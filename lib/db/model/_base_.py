class BaseModel(object):
    #more common fields+methods among model classes to be here
    pass

from sqlalchemy.ext.declarative import declarative_base
DeclarativeBase = declarative_base(cls=BaseModel)
