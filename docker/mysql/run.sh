docker run -p 3306:3306 --name gmysql \
    -e MYSQL_ROOT_PASSWORD=creepy \
    -e MYSQL_DATABASE=creepy -d mysql \
    --character-set-server=utf8 \
    --collation-server=utf8_unicode_ci
