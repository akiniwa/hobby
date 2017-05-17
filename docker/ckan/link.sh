docker run --name ckan \
	-p 5000:5000       \
    --link redis:redis \
    --link db:db       \
    --link solr:solr   \
    -d ckan/ckan;
