from sqlalchemy.orm import Mapped, mapped_column

from database import Base



class UserOrm(Base):
    __tablename__ = "users"


    id : Mapped[int] = mapped_column(primary_key=True)
    first_name : Mapped[str]
    last_name : Mapped[str]
    age : Mapped[int]
