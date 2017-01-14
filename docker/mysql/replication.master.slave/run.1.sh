echo 'step 1 start mysql master and slave'
echo '---> start mysql master'
docker run --name master \
    -e MYSQL_ROOT_PASSWORD=creepy \
    -e MYSQL_DATABASE=creepy \
    -dit -p 33061:3306 \
    -v `pwd`/master/conf.d:/etc/mysql/mysql.conf.d/ \
    -v `pwd`/master/data:/var/lib/mysql \
    -v `pwd`/master/log:/var/log/mysql \
    -v `pwd`/master/backup:/backup \
    -h master mysql

echo '---> start mysql slave'
docker run --name slave --link master \
    -e MYSQL_ROOT_PASSWORD=creepy \
    -e MYSQL_DATABASE=creepy \
    -dit -p 33062:3306 \
    -v `pwd`/slave/conf.d:/etc/mysql/mysql.conf.d/ \
    -v `pwd`/slave/data:/var/lib/mysql \
    -v `pwd`/slave/log:/var/log/mysql \
    -v `pwd`/slave/backup:/backup \
    -h slave mysql

echo 'step 2 setup mysql master hosts'
echo '---> get mysql slaveip'
# find out ip address of slave
slaveip=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' slave)
echo '---> setup mysql master hosts'
# append the new ip as new host entry in master's host file.
docker exec -i master sh -c "echo '$slaveip slave slave' >> /etc/hosts"
echo '---> check mysql master hosts'
# check if the above command worked
docker exec -i master sh -c "cat /etc/hosts"