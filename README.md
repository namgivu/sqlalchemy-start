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
CAUTION clear every thing ie. container+volume
```bash
docker-compose down -v #ref. https://stackoverflow.com/a/45512667/248616
```
