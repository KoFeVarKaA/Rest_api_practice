import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import asyncio
import enum
from sqlalchemy import ForeignKey, func, insert, select, text, Table, Column, Integer, String, MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import URL, create_engine, text
from typing import Annotated

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

class UsersOrm(Base):
    __tablename__ = "users"


    id : Mapped[int] = mapped_column(primary_key=True)
    first_name : Mapped[str]
    last_name : Mapped[str]
    age : Mapped[int]

class SyncORM:
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = False

    @staticmethod
    def del_one(user_id):
        with session_factory() as session:
            obj = session.get(UsersOrm, user_id)
            session.delete(obj)
            session.commit()

    @staticmethod
    def insert_user(user):
        with session_factory() as session:
            session.add(user)
            session.commit()

    @staticmethod
    def insert_users():
        user_1 = UsersOrm(
            first_name='user1',
            last_name='last_name1',
            age=130,
            )
        user_2 = UsersOrm(
            first_name='user2',
            last_name='last_name2',
            age=20,
        )
        user_3 = UsersOrm(
            first_name='user3',
            last_name='last_name666',
            age=20,
        )
        with session_factory() as session:
            session.add_all([user_1, user_2, user_3])
            session.commit()

    @staticmethod
    def select_user_id(user_id):
        with session_factory() as session:
            user = session.get(UsersOrm, {"id": user_id})
            return user
            
    @staticmethod
    def select_users_all():
        with session_factory() as session:
            query = select(UsersOrm) 
            res = session.execute(query)
            users = res.scalars().all()
            return users

    @staticmethod
    def update_users(user_id : int = 1, new_username : str = "Kostya"):
        with session_factory() as session:
            #Сначала получаем объект и только потом его обновляем!
            user = session.get(UsersOrm, user_id)
            #Потом работаем с атрибутами
            user.username = new_username
            #expire() или expire_all()Чтобы сбросить все изменения в сессии
            #refresh() -  не не посылать, а вернуть исходное зн. из бд, обновить данные в питоне на актуальные
            session.commit()

SyncORM.create_tables()
SyncORM.insert_users()
SyncORM.select_users_all()