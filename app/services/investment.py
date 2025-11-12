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
        if target.fully_invested:
            break

        required = target.full_amount - target.invested_amount
        available = source.full_amount - source.invested_amount
        amount_to_invest = min(required, available)

        if amount_to_invest <= 0:
            continue

        source.invested_amount += amount_to_invest
        target.invested_amount += amount_to_invest

        for obj in (source, target):
            if obj.invested_amount == obj.full_amount:
                obj.fully_invested = True
                if obj.close_date is None:
                    obj.close_date = datetime.now()

        updated_sources.append(source)

    return updated_sources
