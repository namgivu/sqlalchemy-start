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

run01()
