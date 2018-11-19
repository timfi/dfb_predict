from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.orm import relationship

from ..core import Model
from .association_tables import team_season_association_table


__all__ = (
    "Season",
)


class Season(Model):
    __tablename__ = "seasons"

    year = Column(Integer)
    enabled = Column(Boolean, default=True)

    teams = relationship("Team", secondary=team_season_association_table, back_populates="seasons")