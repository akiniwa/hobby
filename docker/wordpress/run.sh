docker run --name gwordpress \
	-p 80:8080 \
	--link gmysql:mysql \
	-e WORDPRESS_DB_USER=root \
	-e WORDPRESS_DB_PASSWORD=creepy \
	-d wordpress