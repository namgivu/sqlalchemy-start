from lib._common_ import *
from lib.db import *
from lib.db.model._all_ import *


def seeding_data():
    engine.execute(delete(User))
    u=User(**dict(name='jsonb int', custom_cols={'int_field':122}));  DbUtil.insert(u)
    u=User(**dict(name='jsonb int', custom_cols={'int_field':None})); DbUtil.insert(u)

def r01():
    seeding_data()
    with DbUtil.get_session() as session:
        r=session.query(User.name, User.custom_cols).filter().all(); pprint(r)

        #jsonb is None
        r=session.query(User.name, User.custom_cols).filter(User.custom_cols['int_field'].astext.is_(None)).all(); pprint(r)

        #jsonb == int value
        #sqlalchemy jsonb cast to python type ref. https://stackoverflow.com/a/44960193/248616
        r=session.query(User.name, User.custom_cols).filter(User.custom_cols['int_field'].astext.cast(Integer)==122).all(); pprint(r)

r01()
