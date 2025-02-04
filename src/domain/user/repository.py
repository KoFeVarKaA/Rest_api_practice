from sqlalchemy import select

from model import sync_engine, Base, session_factory, UsersOrm


class UserRepository:
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
            user = session.get(UsersOrm, user_id)
            user.username = new_username
            session.commit()