docker run --name gwordpress \
    -p 8080:80 \
    --link gmysql:mysql \
    -e WORDPRESS_DB_USER=root \
    -e WORDPRESS_DB_PASSWORD=creepy \
    -d wordpress
