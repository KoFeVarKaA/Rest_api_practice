from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from src.domain.user.model import User
from src.domain.order.model import Order


class UserOrder(Base):
    __tablename__ = "user__order"

    id : Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey('user.id'))
    order_id : Mapped[int] = mapped_column(ForeignKey('order.id'))
    
    
    