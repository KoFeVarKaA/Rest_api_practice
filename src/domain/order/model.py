import enum
from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from src.domain.user.model import User


class StatusEnum(enum.Enum):
    designed = "designed"
    sent = "sent"
    delivered = "delivered"

class Order(Base):
    __tablename__ = "order"


    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str]
    total_amount : Mapped[Numeric] = mapped_column(Numeric(precision=10, scale=2))
    status : Mapped[StatusEnum]
    description : Mapped[str | None]

    users: Mapped[list["User"]] = relationship(secondary="user__order", back_populates="orders")
