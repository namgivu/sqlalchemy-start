from lib.db import *


class User(DeclarativeBase):
    __tablename__ = 'users'

    id           = Column(Integer, primary_key=True, autoincrement=True)
    email        = Column(String)
    name         = Column(String)

    custom_cols  = Column(JSONB, default={})
    extra_info   = Column(MutableDict.as_mutable(JSONB), default={})
    '''
    Why we use Column(MutableDict.as_mutable(JSONB) but not plain `Column(JSONB)?
    --> With plain JSONB, we need to handle the dictionary changes manually, 
        and explicitly save the new changes because it cannot detect the changes automatically.
        However, MutableDict can detect that a value within which has changed 
        and automatically persist the changes to DB object
    '''
