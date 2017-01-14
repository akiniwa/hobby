docker run --name master2 --link master1 \
    -e MYSQL_ROOT_PASSWORD=creepy \
    -e MYSQL_DATABASE=creepy \
    -dit -p 33062:3306 \
    -v `pwd`/master2/conf.d:/etc/mysql/mysql.conf.d/ \
    -v `pwd`/master2/data:/var/lib/mysql \
    -v `pwd`/master2/log:/var/log/mysql \
    -v `pwd`/master2/backup:/backup \
    -h master2 mysql
