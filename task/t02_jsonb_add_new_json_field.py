from lib.db             import *
from lib.db.model._all_ import *
from lib._common_       import *


def r0():
    users = DbUtil.run_sql('''
    select JSONB_SET(
        '{}',
        '{new_field}',
        '{"kkk": "vvv"}',
        TRUE
    )
    ''')
    pprint([u for u in users])


def r1():
    users = DbUtil.run_sql('''
    select * from users;
    ''')
    pprint([u for u in users])

def r2a_add_new_field():
    rows = DbUtil.run_sql('''
    select JSONB_SET(
        u.custom_cols,
        '{new_field}',
        '{"kkk": "vvv"}',
        TRUE
    )
    from users u;
    ''')
    pprint([r for r in rows])

def r2b_add_new_field():
    DbUtil.run_sql('''
    update users set custom_cols=JSONB_SET(
        custom_cols,
        '{new_field}',
        '{"kkk": "vvv"}',
        TRUE -- new_value added if create_missing is true ref. https://www.postgresql.org/docs/9.5/static/functions-json.html
    );
    ''')
    rows = User.find_all()
    pprint([r for r in rows])

def r2c_add_new_field():
    DbUtil.run_sql('''
    update users set custom_cols=JSONB_SET(
        custom_cols,
        '{new_field}',
        '1.22',
        TRUE -- new_value added if create_missing is true ref. https://www.postgresql.org/docs/9.5/static/functions-json.html
    );
    ''')
    rows = User.find_all()
    pprint([r for r in rows])

def r2d_add_new_field():
    DbUtil.run_sql('''
    update users set custom_cols=JSONB_SET(
        custom_cols,
        '{new_field}',
        'null', -- set null for json value ref. https://stackoverflow.com/a/21121251/248616 --TODO how to delete it completedly
        TRUE    -- new_value added if create_missing is true ref. https://www.postgresql.org/docs/9.5/static/functions-json.html
    );
    ''')
    rows = User.find_all()
    pprint([r for r in rows])

def r2e_add_new_field():
    DbUtil.run_sql('''
    update users set custom_cols=JSONB_SET(
        custom_cols,
        '{new_field}',
        'true', -- boolean type in json
        TRUE    -- new_value added if create_missing is true ref. https://www.postgresql.org/docs/9.5/static/functions-json.html
    );
    ''')
    rows = User.find_all()
    pprint([r for r in rows])

r1()
r2e_add_new_field()
