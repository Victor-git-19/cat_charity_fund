from datetime import datetime
from typing import Iterable, List

from app.models.abstract_model import InvestmentModel


def investment(
    target: InvestmentModel,
    sources: Iterable[InvestmentModel],
) -> List[InvestmentModel]:
    """
    Распределяет объекты sources по target в порядке FIFO.
    Возвращает список источников, которые были изменены.
    """
    updated_sources: List[InvestmentModel] = []
    for source in sources:
        updated_sources.append(source)
        amount_to_invest = min(
            target.full_amount - target.invested_amount,
            source.full_amount - source.invested_amount,
        )

        for obj in (source, target):
            obj.invested_amount += amount_to_invest
            if obj.invested_amount == obj.full_amount:
                obj.fully_invested = True
                obj.close_date = datetime.now()

        if target.fully_invested:
            break

    return updated_sources
