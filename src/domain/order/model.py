from sqlalchemy import Numeric
from sqlalchemy.orm import Mapped, mapped_column

from database import Base



class Order(Base):
    __tablename__ = "order"


    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str]
    total_sum : Mapped[Numeric] = mapped_column(Numeric(precision=10, scale=2))
  