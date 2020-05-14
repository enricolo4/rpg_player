from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from persitence.base_dbo import BaseDBO
from shared.singleton import Singleton

options = {
    'pool_recycle': 3600,
    'pool_size': 10,
    'pool_timeout': 30,
    'max_overflow': 30,
    'echo': True,
    'execution_options': {
        'autocommit': True
    }
}


class SQLAlchemySession(metaclass=Singleton):
    def __init__(self):
        self.__engine = self.__create_engine()
        self.__session = scoped_session(sessionmaker())
        self.__init_session()
        self.__environment()

    @property
    def session(self):
        return self.__session

    def __init_session(self):
        self.__session.configure(bind=self.__engine)

    @classmethod
    def __create_engine(cls):
        db_engine = "sqlite:///rpg_player.sqlite3"
        return create_engine(db_engine)

    def __environment(self):
        BaseDBO.metadata.drop_all(self.__engine, checkfirst=True)
        BaseDBO.metadata.create_all(self.__engine)
