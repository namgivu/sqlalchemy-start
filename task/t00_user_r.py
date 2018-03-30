from lib.db.mysql       import *
from lib.db.model._all_ import *
from lib._common_       import *

with MySqlUtil.get_session() as session:
    users = session.query(User).all()
    pprint(users)
