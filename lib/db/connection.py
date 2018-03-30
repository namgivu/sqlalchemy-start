class DbProvider:
    MYSQL    = 'mysql'
    POSTGRES = 'postgres'

def get_connection_string(provider):
    if False: pass

    elif provider==DbProvider.MYSQL:
        connection_string = 'mysql+pymysql://{user}:{pswd}@{host}:{port}/{db}?charset=utf8'.format(
            user='root',
            pswd='root',
            host='localhost',
            port='33066',
              db='sqlalchemy_start',
        )
        return connection_string

    else: raise Exception('Db provider not supported "%s"' % provider)
