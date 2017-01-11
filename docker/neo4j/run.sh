# disable authentication
docker run --rm \
    --env=NEO4J_AUTH=none \
    --publish=7474:7474 \
    --publish=7687:7687 \
    --volume=$HOME/neo4j/data:/data \
    --volume=$HOME/neo4j/logs:/logs \
    --name gneo4j neo4j
# default
# username: neo4j
# password: neo4j
