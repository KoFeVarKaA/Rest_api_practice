from sqlalchemy import select

from model import Base, UserOrm
from database import sync_engine, session_factory


class UserRepository:

    @staticmethod
    def del_one(user_id):
        with session_factory() as session:
            obj = session.get(UserOrm, user_id)
            session.delete(obj)
            session.commit()

    @staticmethod
    def insert_user(user):
        with session_factory() as session:
            session.add(user)
            session.commit()

    @staticmethod
    def select_user_id(user_id):
        with session_factory() as session:
            user = session.get(UserOrm, {"id": user_id})
            return user
            
    @staticmethod
    def select_users_all():
        with session_factory() as session:
            query = select(UserOrm) 
            res = session.execute(query)
            users = res.scalars().all()
            return users

    @staticmethod
    def update_users(user_id : int = 1, new_username : str = "Kostya"):
        with session_factory() as session:
            user = session.get(UserOrm, user_id)
            user.username = new_username
            session.commit()