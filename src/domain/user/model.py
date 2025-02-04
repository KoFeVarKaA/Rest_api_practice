from sqlalchemy.orm import sessionmaker, Mapped, mapped_column
from sqlalchemy import create_engine

from database import Base

import config

sync_engine = create_engine(
    url = config.settings.DATABASE_URL_psycopg,
    echo = True, 
    pool_size = 5,
    max_overflow = 10
)

session_factory = sessionmaker(sync_engine)


class UsersOrm(Base):
    __tablename__ = "users"


    id : Mapped[int] = mapped_column(primary_key=True)
    first_name : Mapped[str]
    last_name : Mapped[str]
    age : Mapped[int]
