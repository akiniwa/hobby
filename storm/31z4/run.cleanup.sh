echo '----- stop containers -----'
docker stop zookeeper nimbus supervisor

echo '----- remove containers -----'
docker rm zookeeper nimbus supervisor

echo '----- list all containers -----'
docker ps -a
