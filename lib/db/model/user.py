from lib.db.mysql import *


class User(DeclarativeBase):
    __tablename__ = 'users'

    id    = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    name  = Column(String)

