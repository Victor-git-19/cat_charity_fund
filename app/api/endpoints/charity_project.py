from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (check_charity_project_name_duplicate,
                                validate_charity_project_delete,
                                validate_charity_project_exists,
                                validate_charity_project_update)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectDB,
                                         CharityProjectUpdate)
from app.services.investment import investment

router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)]
)
async def create_charity_project(
        charity_project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session),
):
    """Создание проекта - только для суперюзеров."""
    await check_charity_project_name_duplicate(charity_project.name, session)
    new_project = await charity_project_crud.create(
        charity_project, session, commit=False
    )
    donations = await donation_crud.get_not_fully_invested(session)
    investment(new_project, donations)
    await session.commit()
    await session.refresh(new_project)
    return new_project


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_charity_projects(
        session: AsyncSession = Depends(get_async_session),
):
    """Получение всех проектов - доступно всем."""
    return await charity_project_crud.get_multi(session)


@router.patch(
    '/{charity_project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)]
)
async def partially_update_charity_project(
        charity_project_id: int,
        obj_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    """Обновление проекта - только для суперюзеров."""
    project = await charity_project_crud.get(charity_project_id, session)
    project = validate_charity_project_exists(project)
    validate_charity_project_update(project, obj_in)
    if obj_in.name is not None:
        await check_charity_project_name_duplicate(obj_in.name, session)
    return await charity_project_crud.update(project, obj_in, session)


@router.delete(
    '/{charity_project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)]
)
async def delete_charity_project(
        charity_project_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """Удаление проекта - только для суперюзеров."""
    project = await charity_project_crud.get(charity_project_id, session)
    project = validate_charity_project_exists(project)
    validate_charity_project_delete(project)
    return await charity_project_crud.remove(project, session)
