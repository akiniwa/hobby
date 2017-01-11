docker run --name redis -p 6379:6379 -d redis;
docker run --name db    -p 5432:5432 -d ckan/postgresql;
docker run --name solr  -p 8983:8983 -d ckan/solr;
