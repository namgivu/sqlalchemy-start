from lib.db             import *
from lib.db.model._all_ import *
from lib._common_       import *


def run01a():
    """
    get a raw, compiled SQL query from a SQLAlchemy expression ref. https://stackoverflow.com/a/25563491/248616
    simple query
    """
    with DbUtil.get_session() as session:
        q = session.query(User)
        from sqlalchemy.dialects import postgresql
        sql=str(
            q.statement.compile(dialect=postgresql.dialect())
        )
        print(sql)


def run01b():
    """
    get a raw, compiled SQL query from a SQLAlchemy expression ref. https://stackoverflow.com/a/25563491/248616
    simple query
    """
    with DbUtil.get_session() as session:
        q = session.query(User)
        sql_mysql    = DbUtil.get_raw_sql(sqlalchemy_expression=q, sql_dialect=DIALECT_MYSQL)
        sql_postgres = DbUtil.get_raw_sql(sqlalchemy_expression=q, sql_dialect=DIALECT_POSTGRES)
        print('#sql_mysql   \n%s'% sql_mysql)
        print()
        print('#sql_postgres\n%s'% sql_postgres)


def run02a():
    """
    CRUD query
    ref. https://stackoverflow.com/a/37842617/248616
    """
    q   = update(User).values(name='some name')
    sql = q.compile(dialect=DIALECT_POSTGRES, compile_kwargs={"literal_binds": True})
    print(sql)

    q   = insert(User).values(name='some name')
    sql = q.compile(dialect=DIALECT_POSTGRES, compile_kwargs={"literal_binds": True})
    print(sql) #TODO how to limit users' columns listing to be exact as .values(col1='val1', ...) call?

    '''sample output
UPDATE users SET name='some name'
INSERT INTO users (id, name, custom_cols, extra_info) VALUES (%(id)s, 'some name', %(custom_cols)s, %(extra_info)s) #TODO how to limit users' columns listing to be exact as .values(col1='val1', ...) call?
    '''


def run02b():
    """
    CRUD query
    ref. https://stackoverflow.com/a/37842617/248616
    """
    q   = update(User).values(name='some name')
    sql = DbUtil.get_raw_sql(sqlalchemy_statement=q, sql_dialect=DIALECT_POSTGRES)
    print(sql)

    q   = insert(User).values(name='some name')
    sql = DbUtil.get_raw_sql(sqlalchemy_statement=q, sql_dialect=DIALECT_POSTGRES)
    print(sql) #TODO how to limit users' columns listing to be exact as .values(col1='val1', ...) call?

    '''sample output
UPDATE users SET name='some name'
INSERT INTO users (id, name, custom_cols, extra_info) VALUES (%(id)s, 'some name', %(custom_cols)s, %(extra_info)s) #TODO how to limit users' columns listing to be exact as .values(col1='val1', ...) call?
    '''

run02b()
