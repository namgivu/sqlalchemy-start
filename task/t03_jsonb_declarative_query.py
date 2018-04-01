from lib.db             import *
from lib.db.model._all_ import *
from lib._common_       import *


def seeding_data():
    engine.execute(delete(User))
    u=User(**dict(name='1',   custom_cols={'k':'1'}));  DbUtil.insert(u)
    u=User(**dict(name='22',  custom_cols={'k':'22'})); DbUtil.insert(u)
    u=User(**dict(name='ccf', custom_cols={'custom_cols_field':'ccf'})); DbUtil.insert(u)

def r01():
    seeding_data()
    with DbUtil.get_session() as session:
        r=session.query(User.name, User.custom_cols).filter(User.name=='1').all(); print(r)
        r=session.query(User.name, User.custom_cols).filter(User.custom_cols['k'].astext=='1').all(); print(r)

def r02():
    seeding_data()
    with DbUtil.get_session() as session:
        r=session.query(User.name, User.custom_cols).filter(User.custom_cols['custom_cols_field'].astext=='ccf').all(); print(r)

        #region update via .custom_cols['custom_cols_field']
        r=session.query(User).filter(User.name=='ccf').all()
        assert len(r)>0 ; u=r[0]
        print(u.custom_cols['custom_cols_field'])
        u.custom_cols['custom_cols_field'] = 'new new'; session.add(u); session.commit()
        r=session.query(User.name, User.custom_cols).filter(User.name=='ccf').all(); print(r)
        #endregion

        #region update via .custom_cols_field
        r=session.query(User).filter(User.name=='ccf').all()
        assert len(r)>0 ; u=r[0]
        print(u.custom_cols_field)
        u.custom_cols_field = 'wen wen'; session.add(u); session.commit()
        r=session.query(User.name, User.custom_cols).filter(User.name=='ccf').all(); print(r)
        #endregion

r02()
