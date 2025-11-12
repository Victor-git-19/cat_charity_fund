from datetime import datetime

from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Integer

from app.constants import DEFAULT_AMOUNT
from app.core.db import Base


class InvestmentModel(Base):
    """Базовая модель для пожертвований и проектов."""
    __abstract__ = True

    full_amount = Column(
        Integer,
        CheckConstraint('full_amount > 0'),
        nullable=False,
    )
    invested_amount = Column(
        Integer,
        CheckConstraint(
            'invested_amount >= 0 AND invested_amount <= full_amount'),
        default=DEFAULT_AMOUNT,
        nullable=False,
    )
    fully_invested = Column(Boolean, default=False, nullable=False)
    create_date = Column(DateTime, default=datetime.now, nullable=False)
    close_date = Column(DateTime)

    def __repr__(self):
        return (
            f'{self.__class__.__name__}'
            f'(id={self.id}, full_amount={self.full_amount}, '
            f'invested_amount={self.invested_amount}, '
            f'fully_invested={self.fully_invested})'
        )
