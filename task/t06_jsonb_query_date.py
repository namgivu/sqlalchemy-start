from lib.db       import *
from lib._common_ import *
from lib.db.model._all_ import *


def seeding_data():
    engine.execute(delete(User))
    u=User(**dict(name='jsonb date', custom_cols={'date_field':datetime.utcnow().date()})); DbUtil.insert(u)
    u=User(**dict(name='jsonb date', custom_cols={'date_field':None}));                     DbUtil.insert(u)

def r01():
    seeding_data()
    with DbUtil.get_session() as session:
        r=session.query(User.name, User.custom_cols).filter().all(); pprint(r)

        #jsonb is None
        r=session.query(User.name, User.custom_cols).filter(
            User.custom_cols['date_field'].astext.is_(None)
        ).all(); pprint(r)

        #jsonb == date value
        #sqlalchemy jsonb cast to python type ref. https://stackoverflow.com/a/44960193/248616
        r=session.query(User.name, User.custom_cols).filter(
            User.custom_cols['date_field'].astext.cast(Date)==datetime.utcnow().date()
        ).all(); pprint(r)

r01()
