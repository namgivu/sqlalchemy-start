#get-started
##start mysql container
```bash
docker-compose up #mysql container at port 33066 (NOT 3306 the default mysql port)
```

##create db
choose database provider to work with eg. postgres
```sql
DROP DATABASE IF EXISTS sqlalchemy_start;
CREATE DATABASE         sqlalchemy_start;
```

##table users
```postgresql
DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL,
  email       varchar(63),
  name        varchar(63),
  extra_info  jsonb default '{}'::jsonb,
  custom_cols jsonb default '{}'::jsonb,
  PRIMARY KEY (id)
);

```

```mysql
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(63),
  `name`  varchar(63),
  PRIMARY KEY (`id`)
) ENGINE=InnoDb DEFAULT CHARSET=utf8;

```

#config python app
CODE='/path/to/sqlalchemy-start/git-cloned'
Config at file `$CODE/config`


#clean up
```bash
#turn off container but keep volumns
docker-compose down

#CAUTION clear every thing ie. container+volume
docker-compose down -v #ref. https://stackoverflow.com/a/45512667/248616
```

#JSONB w/ sqlalchemy intro ref
https://gist.github.com/sebflipper/e95d12d72492fbab1b08
https://www.compose.com/articles/using-json-extensions-in-postgresql-from-python-2/

jsonb raw sql function
https://www.postgresql.org/docs/9.5/static/functions-json.html
https://stackoverflow.com/a/46799159/248616
