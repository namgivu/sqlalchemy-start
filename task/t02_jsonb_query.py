from lib.db             import *
from lib.db.model._all_ import *
from lib._common_       import *


def r1():
    users = DbUtil.run_sql('''
    select * from users;
    ''')
    pprint([u for u in users])

r1()
