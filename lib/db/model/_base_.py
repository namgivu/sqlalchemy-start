class BaseModel(object):

    @classmethod
    def find_all(cls):
        from lib.db.mysql import MySqlUtil
        with MySqlUtil.get_session() as session:
            rows = session.query(cls).all()
            return rows

    #more common fields+methods among model classes to be here

from sqlalchemy.ext.declarative import declarative_base
DeclarativeBase = declarative_base(cls=BaseModel)
