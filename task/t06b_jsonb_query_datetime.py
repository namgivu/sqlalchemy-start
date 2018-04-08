from lib.db       import *
from lib._common_ import *
from lib.db.model._all_ import *

import pytz

sgt = pytz.timezone('Asia/Singapore')
utc = pytz.timezone('UTC')
sgt_now = sgt.localize(datetime.utcnow())
utc_now = utc.localize(datetime.utcnow())

def seeding_data():
    engine.execute(delete(User))
    u=User(**dict(name='jsonb datetime utc',  custom_cols={'datetime_field':utc_now})); DbUtil.insert(u)
    u=User(**dict(name='jsonb datetime sgt',  custom_cols={'datetime_field':sgt_now})); DbUtil.insert(u)
    u=User(**dict(name='jsonb datetime none', custom_cols={'datetime_field':None}));    DbUtil.insert(u)

def r01():
    seeding_data()
    with DbUtil.get_session() as session:
        r=session.query(User.name, User.custom_cols)                                        .all(); pprint(r)
        r=session.query(User.name, User.custom_cols['datetime_field'].astext)               .all(); pprint(r)
        r=session.query(User.name, User.custom_cols['datetime_field'].astext.cast(DateTime)).all(); pprint(r)

        #jsonb is None
        r=session.query(User.name, User.custom_cols).filter(User.custom_cols['datetime_field'].astext.is_(None)).all(); pprint(r)

        #jsonb == datetime value
        #sqlalchemy jsonb cast to python type ref. https://stackoverflow.com/a/44960193/248616
        r=session.query(User.name, User.custom_cols).filter(User.custom_cols['datetime_field'].astext.cast(DateTime)==utc_now).all(); pprint(r)
        r=session.query(User.name, User.custom_cols).filter(User.custom_cols['datetime_field'].astext.cast(DateTime)==sgt_now).all(); pprint(r)
        r=session.query(User.name, User.custom_cols).filter(User.custom_cols['datetime_field'].astext.cast(String)==str(sgt_now)).all(); pprint(r)
        r=session.query(User.name, User.custom_cols).filter(User.custom_cols['datetime_field'].astext.cast(String)==str(utc_now)).all(); pprint(r)

r01()
