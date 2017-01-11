docker run --name ckan  -p 80:5000   \
    --link redis:redis        \
    --link db:ckan/postgresql \
    --link solr:ckan/solr     \
    -d ckan/ckan;