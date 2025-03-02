import enum
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

if TYPE_CHECKING:
   from src.domain.user.model import User



class ProfessionEnum(enum.Enum):
    Frontend_Developer: str = "Frontend_Developer"
    Data_Scientist: str = "Data_Scientist"
    DevOps_Engineer: str = "DevOps_Engineer"
    Backend_Developer: str = "Backend_Developer"
    Game_Developer: str = "Game_Developer"
    Machine_Learning_Engineer: str = "Machine_Learning_Engineer"

class Profession(Base):
    __tablename__ = "profession"

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[ProfessionEnum]

    users: Mapped[list["User"]] = relationship()