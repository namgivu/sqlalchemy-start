from lib.db             import *
from lib.db.model._all_ import *
from lib._common_       import *


def run01():
    with DbUtil.get_session() as session:
        users = session.query(User).all()
        pprint(users)


def run02():
    users = User.find_all()
    pprint(users)


def run03():
    u = User(**dict(
        email = 'some@eemail.com',
        name  = 'Some Name',
    ))
    pprint(u.to_dict())


def run04():
    u = User(**dict(
        email = 'some@eemail.com',
        name  = 'Some Name',
    ))
    DbUtil.insert(u)

    users = User.find_all()
    pprint(users)

run04()
