from lib.db import *


class User(DeclarativeBase):
    __tablename__ = 'users'

    id          = Column(Integer, primary_key=True, autoincrement=True)
    email       = Column(String)
    name        = Column(String)

    extra_info  = Column(JSONB, default={})
    custom_cols = Column(MutableDict.as_mutable(JSONB), default={})
    '''
    Why we use Column(MutableDict.as_mutable(JSONB) but not plain `Column(JSONB)?
    --> Simply that JSONB cannot record updates while MutableDict.as_mutable(JSONB) can
    '''

    #region custom_cols_field --> custom_cols.custom_cols_field column
    '''c#-alike property for python with sqlalchemy ref. https://stackoverflow.com/a/3324965/248616, sqlalchemy hybrid-property ref2. https://stackoverflow.com/a/31915355/248616'''
    @property
    def custom_cols_field(self): f='custom_cols_field'; return self.custom_cols[f] if f in self.custom_cols else None

    @custom_cols_field.setter #IMPORTANT NOTE: custom_cols_field == method name above
    def custom_cols_field(self, value): f='custom_cols_field'; self.custom_cols[f] = value
    #endregion
