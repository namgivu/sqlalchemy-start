class BaseModel(object):

    @classmethod
    def get_columns(cls):
        return cls.metadata.tables[cls.__tablename__].columns.keys()

    def to_dict(self):
        """
        01 convert *model_obj.column* to *dict['column']*
        02 also convert *sqlalchemy-hybrid attributes* if any
        """
        d = {}

        #region extract db columns to dict
        columns = self._sa_class_manager.mapper.mapped_table.columns
        for c in columns:
            d[c.name] = getattr(self, c.name)

        #alternative implementation
        #return {c.key: getattr(self, c.key)
        #    for c in inspect(self).mapper.column_attrs}

        pass
        #endregion extract db columns

        #region extract hybrid property to dict
        '''ref. https://stackoverflow.com/a/31869608/248616'''
        from sqlalchemy.inspection import inspect as sa_inspect
        from sqlalchemy.ext.hybrid import hybrid_property
        for item in sa_inspect(self.__class__).all_orm_descriptors:
            if type(item) == hybrid_property:
                ha = item.__name__ #ha means hybrid-property attribute aka. hybrid attribute
                d[ha] = getattr(self, ha)
        #endregion extract hybrid property

        return d

    def __repr__(self):
        from pprint import pformat
        return pformat(self.to_dict())

    @classmethod
    def find_all(cls):
        from lib.db import DbUtil
        with DbUtil.get_session() as session:
            rows = session.query(cls).all()
            return rows

    #more common fields+methods among model classes to be here


from sqlalchemy.ext.declarative import declarative_base
DeclarativeBase = declarative_base(cls=BaseModel)
