from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.abstract_model import InvestmentModel


class Donation(InvestmentModel):
    """Модель пожертвований."""
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
