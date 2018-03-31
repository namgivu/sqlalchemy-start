from lib.db             import *
from lib.db.model._all_ import *
from lib._common_       import *


def run01():
    with DbUtil.get_session() as session:
        q = session.query(User)
        from sqlalchemy.dialects import postgresql
        sql=str(
            q.statement.compile(dialect=postgresql.dialect())
        ) #get a raw, compiled SQL query from a SQLAlchemy expression ref. https://stackoverflow.com/a/25563491/248616
        print(sql)


def run02():
    with DbUtil.get_session() as session:
        q = session.query(User)
        sql_mysql    = DbUtil.get_raw_sql(q, DIALECT_MYSQL)
        sql_postgres = DbUtil.get_raw_sql(q, DIALECT_POSTGRES)
        print('#sql_mysql   \n%s'% sql_mysql)
        print()
        print('#sql_postgres\n%s'% sql_postgres)


run02()
