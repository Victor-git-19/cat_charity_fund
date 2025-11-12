from sqlalchemy import Column, String, Text

from app.constants import MAX_LENGTH
from app.models.abstract_model import InvestmentModel


class CharityProject(InvestmentModel):
    """Модель проектов."""
    name = Column(String(MAX_LENGTH), unique=True, nullable=False)
    description = Column(Text)
