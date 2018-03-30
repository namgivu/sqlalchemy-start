#region connection as session
from contextlib import contextmanager

from sqlalchemy     import create_engine
from sqlalchemy.orm import sessionmaker
connection_string = 'mysql+pymysql://{user}:{pswd}@{host}:{port}/{db}?charset=utf8'.format(
    user='root',
    pswd='root',
    host='localhost',
    port='33066',
      db='sqlalchemy_start',
)
engine  = create_engine(connection_string)
Session = sessionmaker(bind=engine)
#endregion connection as session


#util
class MySqlUtil:

    @classmethod
    @contextmanager #this helps to get around the error 'AttributeError: __exit__' #TODO why is that?
    def get_session(cls):
        """
        IMPORTANT NOTE
        we are creating a python generator ref. https://stackoverflow.com/a/231855/248616, NOT a normal method
        *yield* is used in place of *return* #TODO master this point, what the h*** is this ^^?
        """
        session = Session(expire_on_commit=False)
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()


    @classmethod
    def insert(cls, model_instance):
        with cls.get_session() as session:
            session.add(model_instance)
            session.commit()
            session.refresh(model_instance)
            return model_instance


    @classmethod
    def update(cls, model_instance):
        """
        In sqlalchemy, update+insert are same when saving to db
        """
        with cls.get_session() as session:
            session.add(model_instance)
            session.commit()
            session.refresh(model_instance)
            return model_instance


#common import among model classes
from lib.db.model._base_ import DeclarativeBase
from sqlalchemy import Column, UniqueConstraint, ForeignKey
from sqlalchemy import String, Integer, SmallInteger, BigInteger, DateTime, Float
