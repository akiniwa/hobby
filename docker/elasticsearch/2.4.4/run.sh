docker run --name es244 \
	-p9200:9200 -p9300:9300 \
	-d elasticsearch:2.4.4 \
	-Des.node.name="es244"