docker run --name postgres \
    -e POSTGRES_PASSWORD=creepy \
    -e POSTGRES_USER=creepy \
    -e POSTGRES_DB=creepy \
    -d postgres