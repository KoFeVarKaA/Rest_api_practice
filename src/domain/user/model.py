from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from src.domain.profession.model import Profession
# from src.domain.order.model import Order


class User(Base):
    __tablename__ = "user"


    id : Mapped[int] = mapped_column(primary_key=True)
    first_name : Mapped[str]
    last_name : Mapped[str]
    age : Mapped[int]
    profession_id : Mapped[int | None] = mapped_column(ForeignKey('profession.id'))

    profession: Mapped["Profession | None"] = relationship(back_populates="users")
    orders: Mapped[list["Order"]] = relationship(secondary="user__order", back_populates="users")
