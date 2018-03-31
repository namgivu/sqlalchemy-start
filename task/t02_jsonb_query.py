from lib.db             import *
from lib.db.model._all_ import *
from lib._common_       import *


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
        '{"value": "v2"}',
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
        TRUE
    );
    ''')
    rows = User.find_all()
    pprint([r for r in rows])

r2b_add_new_field()
