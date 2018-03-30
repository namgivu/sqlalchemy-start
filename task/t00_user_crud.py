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

def run05():
    u = User()
    u.extra_info = dict(
        field1=122,
        field2='abb',
    )
    DbUtil.insert(u)

    users = User.find_all()
    pprint(users)

    with DbUtil.get_session() as session:
        r = session.query(User).filter(User.extra_info['field1'].astext=='122').all()
        pprint(r)

run05()
