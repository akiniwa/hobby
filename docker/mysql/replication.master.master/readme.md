### steps

1. config and data folder

    1. folder

            server#/backup
            server#/data
            server#/log
            server#/conf.d

    1. config master1

            # master1/conf.d/master1.cnf
            [mysqld]
                server-id = 101
                log_bin = /var/log/mysql/mysql-bin.log
                binlog_do_db = creepy
                # make sure to bind it to all IPs, else mysql listens on 127.0.0.1
                bind-address = 0.0.0.0
                character_set_server = utf8
                collation_server = utf8_general_ci
             
            [mysql]
                default_character_set = utf8

            # master1/backup/initdb.sql
            use mysql;
            create user 'replicator'@'%' identified by 'creepy';
            grant replication slave on *.* to 'replicator'@'%';
            # do note that the replicator permission cannot be granted on single database. 
            FLUSH PRIVILEGES;
            SHOW MASTER STATUS;
            SHOW VARIABLES LIKE 'server_id';

    1. config master2

            # master2/conf.d/master2.cnf
            [mysqld]
                # Remember this is only Integer per official documentation
                server-id = 102
                log_bin = /var/log/mysql/mysql-bin.log
                binlog_do_db = creepy
                # make sure to bind it to all IPs, else mysql listens on 127.0.0.1
                bind-address = 0.0.0.0
                character_set_server = utf8
                collation_server = utf8_general_ci
            [mysql]
                default_character_set = utf8

            # master2/backup/initdb.sql
            use mysql;
            create user 'replicator'@'%' identified by 'creepy';
            grant replication slave on *.* to 'replicator'@'%'; 
            # do note that the replicator permission cannot be granted on single database. 
            FLUSH PRIVILEGES;
            SHOW MASTER STATUS;
            SHOW VARIABLES LIKE 'server_id';

1. launch nodes

    1. node1

            $ docker run --name mysql1 -e MYSQL_ROOT_PASSWORD=creepy -e MYSQL_DATABASE=creepy -dit -p 33061:3306 -v /opt2/mysql/master1/conf.d:/etc/mysql/mysql.conf.d/   -v /opt2/mysql/master1/data:/var/lib/mysql -v /opt2/mysql/master1/log:/var/log/mysql -v /opt2/mysql/master1/backup:/backup -h  mysql1 mysql

    1. node2

            $ docker run --name mysql2  <strong>--link mysql1</strong> -e MYSQL_ROOT_PASSWORD=creepy -e MYSQL_DATABASE=creepy -dit -p 33062:3306 -v /opt2/mysql/master2/conf.d:/etc/mysql/mysql.conf.d/   -v /opt2/mysql/master2/data:/var/lib/mysql -v /opt2/mysql/master2/log:/var/log/mysql -v /opt2/mysql/master2/backup:/backup -h  mysql2 mysql

1. link node1 with node2

    1. link

            # find out IP Address of mysql2
            $ mysql2ip=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' mysql2)

            # Append the new IP as new host entry in mysql1's host file.
            $ docker exec -i mysql1 sh -c "echo '$mysql2ip mysql2 mysql2' >> /etc/hosts"

            # Check if the above command worked
            $ docker exec -i mysql1 sh -c "cat /etc/hosts"

    1. check

            $ docker exec -ti mysql2 sh -c "ping mysql1"
            $ docker exec -ti mysql1 sh -c "ping mysql2"

1. create replication users

    1. node1

            $ docker exec -ti mysql1 sh -c "mysql -uroot -p"
            Enter password:
            Welcome to the MySQL monitor.  Commands end with ; or \g.
            Your MySQL connection id is 2
            Server version: 5.7.16-log MySQL Community Server (GPL)

            Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

            Oracle is a registered trademark of Oracle Corporation and/or its
            affiliates. Other names may be trademarks of their respective
            owners.

            Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

            mysql> source /backup/initdb.sql;
            Reading table information for completion of table and column names
            You can turn off this feature to get a quicker startup with -A

            Database changed
            Query OK, 0 rows affected (0.00 sec)

            Query OK, 0 rows affected (0.01 sec)

            Query OK, 0 rows affected (0.00 sec)

            +------------------+----------+--------------+------------------+-------------------+
            | File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
            +------------------+----------+--------------+------------------+-------------------+
            | mysql-bin.000003 |      154 | creepy       |                  |                   |
            +------------------+----------+--------------+------------------+-------------------+
            1 row in set (0.00 sec)

            +---------------+-------+
            | Variable_name | Value |
            +---------------+-------+
            | server_id     | 101   |
            +---------------+-------+
            1 row in set (0.01 sec)

    1. node2

            $ docker exec -ti mysql2 sh -c "mysql -uroot -p"
            Enter password:
            Welcome to the MySQL monitor.  Commands end with ; or \g.
            Your MySQL connection id is 2
            Server version: 5.7.16-log MySQL Community Server (GPL)

            Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

            Oracle is a registered trademark of Oracle Corporation and/or its
            affiliates. Other names may be trademarks of their respective
            owners.

            Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

            mysql> source /backup/initdb.sql;
            Reading table information for completion of table and column names
            You can turn off this feature to get a quicker startup with -A

            Database changed
            Query OK, 0 rows affected (0.01 sec)

            Query OK, 0 rows affected (0.00 sec)

            Query OK, 0 rows affected (0.00 sec)

            +------------------+----------+--------------+------------------+-------------------+
            | File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
            +------------------+----------+--------------+------------------+-------------------+
            | mysql-bin.000003 |      154 | creepy       |                  |                   |
            +------------------+----------+--------------+------------------+-------------------+
            1 row in set (0.00 sec)

            +---------------+-------+
            | Variable_name | Value |
            +---------------+-------+
            | server_id     | 102   |
            +---------------+-------+
            1 row in set (0.01 sec)

1. setup replication source

    1. node1

            $ docker exec -ti mysql2 sh -c "mysql -uroot -p"
            Enter password:
            mysql> stop slave; 
            mysql> CHANGE MASTER TO MASTER_HOST = 'mysql1', MASTER_USER = 'replicator', 
                -> MASTER_PASSWORD = 'creepy', MASTER_LOG_FILE = 'mysql-bin.000003', 
                -> MASTER_LOG_POS = 154; 
            mysql> start slave;
            mysql> show slave status\g

    1. node2

            $ docker exec -ti mysql1 sh -c "mysql -uroot -p"
            Enter password:
            mysql> stop slave; 
            mysql> CHANGE MASTER TO MASTER_HOST = 'mysql2', MASTER_USER = 'replicator', 
                -> MASTER_PASSWORD = 'creepy', MASTER_LOG_FILE = 'mysql-bin.000003',
                -> MASTER_LOG_POS = 154; 
            mysql> start slave;
            mysql> show slave status\g

1. testing master-master replication

    1. create table in `creepy` database in node1 check node2
       
            $ docker exec -ti mysql1 sh -c "mysql -uroot -p"
            Enter password:
            mysql> use creepy;
            mysql> create table students(`id` int, `name` varchar(20));

            $ docker exec -ti mysql2 sh -c "mysql -uroot -p"
            Enter password:
            mysql> show tables in creepy;

    1. remove table from node2 and check node1

            $ docker exec -ti mysql2 sh -c "mysql -uroot -p"
            Enter password:
            mysql> use creepy;
            mysql> drop table students;

            $ docker exec -ti mysql1 sh -c "mysql -uroot -p"
            Enter password:
            mysql> show tables in creepy;
