from pydantic import BaseModel, Field, Extra, PositiveInt, validator
from typing import Optional
from datetime import datetime
from app.constants import MIN_LENGTH, MAX_LENGTH


class CharityProjectCreate(BaseModel):
    name: str = Field(min_length=MIN_LENGTH, max_length=MAX_LENGTH)
    description: str = Field(min_length=MIN_LENGTH)
    full_amount: PositiveInt

    class Config:
        extra = Extra.forbid


class CharityProjectUpdate(BaseModel):
    name: Optional[str] = Field(
        default=None,
        min_length=MIN_LENGTH,
        max_length=MAX_LENGTH
    )
    description: Optional[str] = Field(
        default=None,
        min_length=MIN_LENGTH
    )
    full_amount: Optional[PositiveInt]

    @validator('name', 'description', 'full_amount')
    def validate_fields(cls, value, field):
        if value is None:
            raise ValueError(f'{field.name} не может быть пустым')
        return value

    class Config:
        extra = Extra.forbid


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
