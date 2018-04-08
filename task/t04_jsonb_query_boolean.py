from lib._common_ import *
from lib.db import *
from lib.db.model._all_ import *


def seeding_data():
    engine.execute(delete(User))
    u=User(**dict(name='jsonb bool t', custom_cols={'bool_field':True}));  DbUtil.insert(u)
    u=User(**dict(name='jsonb bool f', custom_cols={'bool_field':False})); DbUtil.insert(u)
    u=User(**dict(name='jsonb bool n', custom_cols={'bool_field':None}));  DbUtil.insert(u)

def r01():
    seeding_data()
    with DbUtil.get_session() as session:
        r=session.query(User.name, User.custom_cols).filter().all(); pprint(r)

        #jsonb is None
        r=session.query(User.name, User.custom_cols).filter(User.custom_cols['bool_field'].astext.is_(None)).all(); pprint(r)

        #jsonb == True/False
        #sqlalchemy jsonb filter compare with True, and sqlalchemy jsonb cast boolean ref. https://stackoverflow.com/a/44960193/248616
        r=session.query(User.name, User.custom_cols).filter(User.custom_cols['bool_field'].astext.cast(Boolean)==True).all(); pprint(r)
        r=session.query(User.name, User.custom_cols).filter(User.custom_cols['bool_field'].astext.cast(Boolean)==False).all(); pprint(r)

r01()
