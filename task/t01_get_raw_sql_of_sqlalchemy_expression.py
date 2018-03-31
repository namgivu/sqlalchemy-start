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
    CRUD query simple
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
    CRUD query simple
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


def run04a():
    """
    JSONB query @ select
    ref. https://stackoverflow.com/a/37842617/248616
    """
    with DbUtil.get_session() as session:
        #region no-limit columns in SELECT clause
        q   = session.query(User)
        sql = DbUtil.get_raw_sql(sqlalchemy_expression=q, sql_dialect=DIALECT_POSTGRES)
        print(sql); print()

        q   = session.query(User).filter(User.name=='abb')
        sql = DbUtil.get_raw_sql(sqlalchemy_expression=q, sql_dialect=DIALECT_POSTGRES)
        print(sql); print()

        q   = session.query(User).filter(User.custom_cols['col1']=='abb')
        sql = DbUtil.get_raw_sql(sqlalchemy_expression=q, sql_dialect=DIALECT_POSTGRES)
        print(sql); print()
        #endregion

        #region limit columns in SELECT clause, with alias
        q   = session.query(User).with_entities(User.name)
        sql = DbUtil.get_raw_sql(sqlalchemy_expression=q, sql_dialect=DIALECT_POSTGRES)
        print(sql); print()

        q   = session.query(User.name) #limit columns in SELECT clause ref. https://stackoverflow.com/a/11535992/248616
        sql = DbUtil.get_raw_sql(sqlalchemy_expression=q, sql_dialect=DIALECT_POSTGRES)
        print(sql); print()

        q   = session.query(User.name.label('some alias name')) #with alias ref. https://stackoverflow.com/a/11535992/248616
        sql = DbUtil.get_raw_sql(sqlalchemy_expression=q, sql_dialect=DIALECT_POSTGRES)
        print(sql); print()

        q   = session.query(User.custom_cols['col1']) #limit columns in SELECT clause
        sql = DbUtil.get_raw_sql(sqlalchemy_expression=q, sql_dialect=DIALECT_POSTGRES)
        print(sql); print()

        q   = session.query(User.custom_cols['col1'].label('some alias name')) #limit columns in SELECT clause
        sql = DbUtil.get_raw_sql(sqlalchemy_expression=q, sql_dialect=DIALECT_POSTGRES)
        print(sql); print()
        #endregion


def run04b():
    """
    JSONB query @ CRUD
    """
    with DbUtil.get_session() as session:
        #read
        q   = session.query(User.custom_cols['col1'].label('some alias name')) #limit columns in SELECT clause
        sql = DbUtil.get_raw_sql(sqlalchemy_expression=q, sql_dialect=DIALECT_POSTGRES)
        print(sql); print()

    #create
    q   = insert(User).values(custom_cols={'col1':122}) #TODO how to get this working?
    sql = DbUtil.get_raw_sql(sqlalchemy_statement=q, sql_dialect=DIALECT_POSTGRES)
    print(sql); print(122)


run04b()
