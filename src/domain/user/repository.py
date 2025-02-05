from sqlalchemy import select

from src.domain.user.model import User
from database import sync_engine, session_factory


class UserRepository:

    @staticmethod
    def del_one(user_id):
        with session_factory() as session:
            obj = session.get(User, user_id)
            session.delete(obj)
            session.commit()

    @staticmethod
    def insert(user):
        with session_factory() as session:
            session.add(user)
            session.commit()

    @staticmethod
    def get_id(user_id):
        with session_factory() as session:
            user = session.get(User, {"id": user_id})
            return user
            
    @staticmethod
    def get_all():
        with session_factory() as session:
            query = select(User) 
            res = session.execute(query)
            users = res.scalars().all()
            return users

    @staticmethod
    def update(user_id : int = 1, new_username : str = "Kostya"):
        with session_factory() as session:
            user = session.get(User, user_id)
            user.username = new_username
            session.commit()