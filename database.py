from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

import config

sync_engine = create_engine(
    url = config.settings.DATABASE_URL_psycopg,
    echo = True, 
    pool_size = 5,
    max_overflow = 10
)

session_factory = sessionmaker(sync_engine)



class Base(DeclarativeBase):
    pass