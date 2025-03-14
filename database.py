from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

import config

async_engine = create_async_engine(
    url = config.settings.DATABASE_URL_asyncpg,
    echo = True, 
    pool_size = 5,
    max_overflow = 10
)

session_factory = async_sessionmaker(async_engine)



class Base(DeclarativeBase):
    pass