from lib.db             import *
from lib.db.model._all_ import *
from lib._common_       import *


def seeding_data():
    engine.execute(delete(User))
    u=User(**dict(name='1',  custom_cols={'k':'1'}));  DbUtil.insert(u)
    u=User(**dict(name='22', custom_cols={'k':'22'})); DbUtil.insert(u)

def r01():
    with DbUtil.get_session() as session:
        r=session.query(User.name, User.custom_cols).filter(User.name=='1').all(); print(r)
        r=session.query(User.name, User.custom_cols).filter(User.custom_cols['k'].astext=='1').all(); print(r)

seeding_data()
r01()
