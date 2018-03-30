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

    elif provider==DbProvider.POSTGRES:
        connection_string = 'postgresql://{user}:{pswd}@{host}:{port}/{db}'.format(
            user='postgres',
            pswd='postgres',
            host='localhost',
            port='54322',
              db='sqlalchemy_start',
        )
        return connection_string

    else: raise Exception('Db provider not supported "%s"' % provider)
