#get-started
start mysql container
```bash
docker-compose up #mysql container at port 33066 (NOT 3306 the default mysql port)
```

create db
```sql
DROP DATABASE IF EXISTS sqlalchemy_start;
CREATE DATABASE         sqlalchemy_start;
```

table users
```sql
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(63),
  `name`  varchar(63),
  PRIMARY KEY (`id`)
) ENGINE=InnoDb DEFAULT CHARSET=utf8;
```
