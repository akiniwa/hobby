echo '----- create zookeeper -----'
docker run -d \
    --restart always \
    --name zookeeper \
    zookeeper:3.4

echo '----- create nimbus -----'
docker run -d \
    --restart always \
    -v /logs -v /data \
    --name nimbus \
    --net container:zookeeper \
    31z4/storm:1.0.2 \
    storm nimbus -c storm.log.dir="/logs" -c storm.local.dir="/data"

echo '----- create supervisor -----'
docker run -d \
    --restart always \
    -v /logs -v /data \
    --name supervisor \
    --net container:nimbus \
    --net container:zookeeper \
    31z4/storm:1.0.2 \
    storm supervisor

echo '----- list all container -----'
docker ps -a
