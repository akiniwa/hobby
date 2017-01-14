echo "step 3 mysql master create replicate user"
docker exec -ti master mysql -uroot -pcreepy -e \
    "use mysql; create user 'replicator'@'%' identified by 'creepy'; grant replication slave on *.* to 'replicator'@'%';  FLUSH PRIVILEGES;" \
    -vvv

echo "step 4 get master status and server_id"
docker exec -ti master mysql -uroot -pcreepy -e \
    "SHOW MASTER STATUS\G" \
    -vvv
docker exec -ti master mysql -uroot -pcreepy -e \
    "SHOW VARIABLES LIKE 'server_id';" \
    -vvv

echo "step 5 setup mysql slave replication"
docker exec -ti slave mysql -uroot -pcreepy -e \
    "stop slave; CHANGE MASTER TO MASTER_HOST = 'master', MASTER_USER = 'replicator', MASTER_PASSWORD = 'creepy', MASTER_LOG_FILE = 'mysql-bin.000003', MASTER_LOG_POS = 154; start slave; show slave status\G" \
    -vvv