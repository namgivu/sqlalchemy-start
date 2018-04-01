#region connection as session
from config import *
assert DB_PROVIDER
from lib.db.connection import *
connection_string = get_connection_string(DB_PROVIDER) #TODO make provider as a config entry

from sqlalchemy     import create_engine
from sqlalchemy.orm import sessionmaker
engine  = create_engine(connection_string)
Session = sessionmaker(bind=engine)
#endregion


#util
class DbUtil:
    from contextlib import contextmanager

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


    @classmethod
    def get_raw_sql(cls, sql_dialect, sqlalchemy_expression=None, sqlalchemy_statement=None):
        """
        :param sql_dialect:            choices    = DIALECT_POSTGRES | DIALECT_MYSQL
        :param sqlalchemy_expression:  sample_exp = session.query(User).all()
        :param sqlalchemy_statement:   sample_stm = session.update(User).values(name='abb')
        :return:
        """

        if sqlalchemy_expression and sqlalchemy_statement:
            raise Exception('Only $sqlalchemy_expression or $sqlalchemy_statement should be provided')

        elif sqlalchemy_expression:
            exp = sqlalchemy_expression #alias $exp means expression
            sql = str(exp.statement.compile(dialect=sql_dialect, compile_kwargs={'literal_binds': True})) #get a raw, compiled SQL query from a SQLAlchemy expression ref. https://stackoverflow.com/a/25563491/248616
            return sql

        elif sqlalchemy_statement is not None: #NOTE we have to use `is not None` here; otherwise, an error occurs 'TypeError: Boolean value of this clause is not defined'
            stm = sqlalchemy_statement #alias $stm means statement
            sql = str(stm.compile(dialect=sql_dialect, compile_kwargs={'literal_binds': True})) #get a raw, compiled SQL query from a SQLAlchemy expression ref. https://stackoverflow.com/a/25563491/248616
            return sql


    @classmethod
    def run_sql(cls, sql):
        """ref. https://stackoverflow.com/a/17987782/248616"""
        from sqlalchemy import text
        return engine.execute(text(sql))


##region common import among model classes

#model base class
from lib.db.model._base_    import DeclarativeBase

#table column type
from sqlalchemy import Column, UniqueConstraint, ForeignKey
from sqlalchemy import String, Integer, SmallInteger, BigInteger, DateTime, Float

#crud command
from sqlalchemy import select, update, insert, delete

#json column
from sqlalchemy.ext.mutable              import MutableDict
from sqlalchemy.dialects.postgresql.json import JSONB

#sql dialect
from sqlalchemy.dialects import postgresql; DIALECT_POSTGRES = postgresql.dialect()
from sqlalchemy.dialects import mysql;      DIALECT_MYSQL    = mysql.dialect()

##endregion
