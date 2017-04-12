docker run --name es522 \
	-p9200:9200 -p9300:9300 \
	-d elasticsearch:5.2.2 \
	-Des.node.name="es522"