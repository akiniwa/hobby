### steps

1. config and data folder

    1. folder

            master/backup
            master/data
            master/log
            master/conf.d

            slave/backup
            slave/data
            slave/log
            slave/conf.d

    1. config master

            # master/conf.d/master.cnf
            [mysqld]
                server-id = 101
                log_bin = /var/log/mysql/mysql-bin.log
                binlog_do_db = creepy
                bind-address = 0.0.0.0
                character_set_server = utf8
                collation_server = utf8_general_ci
             
            [mysql]
                default_character_set = utf8

            # master/backup/initdb.sql
            use mysql;
            create user 'replicator'@'%' identified by 'creepy';
            grant replication slave on *.* to 'replicator'@'%';
            # do note that the replicator permission cannot be granted on single database. 
            FLUSH PRIVILEGES;
            SHOW MASTER STATUS;
            SHOW VARIABLES LIKE 'server_id';

    1. config slave

            # slave/conf.d/slave.cnf
            [mysqld]
                server-id = 102
                bind-address = 0.0.0.0
                character_set_server = utf8
                collation_server = utf8_general_ci

            [mysql]
                default_character_set = utf8

1. launch nodes

    1. master

            $ docker run --name master \
                -e MYSQL_ROOT_PASSWORD=creepy \
                -e MYSQL_DATABASE=creepy \
                -dit -p 33061:3306 \
                -v `pwd`/master/conf.d:/etc/mysql/mysql.conf.d/ \
                -v `pwd`/master/data:/var/lib/mysql \
                -v `pwd`/master/log:/var/log/mysql \
                -v `pwd`/master/backup:/backup \
                -h master mysql

    1. slave

            $ docker run --name slave --link master \
                -e MYSQL_ROOT_PASSWORD=creepy \
                -e MYSQL_DATABASE=creepy \
                -dit -p 33062:3306 \
                -v `pwd`/slave/conf.d:/etc/mysql/mysql.conf.d/ \
                -v `pwd`/slave/data:/var/lib/mysql \
                -v `pwd`/slave/log:/var/log/mysql \
                -v `pwd`/slave/backup:/backup \
                -h slave mysql

1. link master with slave

    1. link

            # find out IP Address of slave
            $ slaveip=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' slave)

            # Append the new IP as new host entry in master's host file.
            $ docker exec -i master sh -c "echo '$slaveip slave slave' >> /etc/hosts"

            # Check if the above command worked
            $ docker exec -i master sh -c "cat /etc/hosts"

    1. check

            $ docker exec -ti slave sh -c "ping master"
            $ docker exec -ti master sh -c "ping slave"

1. create replication users

    1. master

            $ docker exec -ti master sh -c "mysql -uroot -p"
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

1. setup replication source

    1. slave

            $ docker exec -ti slave sh -c "mysql -uroot -p"
            Enter password:
            mysql> stop slave;
            mysql> CHANGE MASTER TO MASTER_HOST = 'master', MASTER_USER = 'replicator', 
                -> MASTER_PASSWORD = 'creepy', MASTER_LOG_FILE = 'mysql-bin.000003', 
                -> MASTER_LOG_POS = 154; 
            mysql> start slave;
            mysql> show slave status\G
            *************************** 1. row ***************************
                           Slave_IO_State: Waiting for master to send event
                              Master_Host: master
                              Master_User: replicator
                              Master_Port: 3306
                            Connect_Retry: 60
                          Master_Log_File: mysql-bin.000003
                      Read_Master_Log_Pos: 154
                           Relay_Log_File: slave-relay-bin.000002
                            Relay_Log_Pos: 320
                    Relay_Master_Log_File: mysql-bin.000003
                         Slave_IO_Running: Yes
                        Slave_SQL_Running: Yes
                          Replicate_Do_DB:
                      Replicate_Ignore_DB:
                       Replicate_Do_Table:
                   Replicate_Ignore_Table:
                  Replicate_Wild_Do_Table:
              Replicate_Wild_Ignore_Table:
                               Last_Errno: 0
                               Last_Error:
                             Skip_Counter: 0
                      Exec_Master_Log_Pos: 154
                          Relay_Log_Space: 527
                          Until_Condition: None
                           Until_Log_File:
                            Until_Log_Pos: 0
                       Master_SSL_Allowed: No
                       Master_SSL_CA_File:
                       Master_SSL_CA_Path:
                          Master_SSL_Cert:
                        Master_SSL_Cipher:
                           Master_SSL_Key:
                    Seconds_Behind_Master: 0
            Master_SSL_Verify_Server_Cert: No
                            Last_IO_Errno: 0
                            Last_IO_Error:
                           Last_SQL_Errno: 0
                           Last_SQL_Error:
              Replicate_Ignore_Server_Ids:
                         Master_Server_Id: 101
                              Master_UUID: cae3f8aa-d808-11e6-8c39-0242ac110002
                         Master_Info_File: /var/lib/mysql/master.info
                                SQL_Delay: 0
                      SQL_Remaining_Delay: NULL
                  Slave_SQL_Running_State: Slave has read all relay log; waiting for more updates
                       Master_Retry_Count: 86400
                              Master_Bind:
                  Last_IO_Error_Timestamp:
                 Last_SQL_Error_Timestamp:
                           Master_SSL_Crl:
                       Master_SSL_Crlpath:
                       Retrieved_Gtid_Set:
                        Executed_Gtid_Set:
                            Auto_Position: 0
                     Replicate_Rewrite_DB:
                             Channel_Name:
                       Master_TLS_Version:
            1 row in set (0.00 sec)


1. testing master-master replication

    1. create table in `creepy` database in master check slave
       
            $ docker exec -ti master sh -c "mysql -uroot -p"
            Enter password:
            mysql> use creepy;
            mysql> create table students(`id` int, `name` varchar(20));
            mysql> show tables in creepy;
            mysql> insert into students values (1, 'gree2');

    1. check table and data in slave

            $ docker exec -ti slave sh -c "mysql -uroot -p"
            Enter password:
            mysql> use creepy;
            mysql> show tables in creepy;
