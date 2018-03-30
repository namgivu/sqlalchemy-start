from lib.db.mysql       import *
from lib.db.model._all_ import *
from lib._common_       import *


def run01():
    with MySqlUtil.get_session() as session:
        users = session.query(User).all()
        pprint(users)


def run02():
    users = User.find_all()
    pprint(users)

run02()
