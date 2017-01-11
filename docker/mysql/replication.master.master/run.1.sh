docker run --name mysql1 \
    -e MYSQL_ROOT_PASSWORD=creepy \
    -e MYSQL_DATABASE=creepy \
    -dit -p 33061:3306 \
    -v `pwd`/master1/conf.d:/etc/mysql/mysql.conf.d/ \
    -v `pwd`/master1/data:/var/lib/mysql \
    -v `pwd`/master1/log:/var/log/mysql \
    -v `pwd`/master1/backup:/backup \
    -h  mysql1 mysql
