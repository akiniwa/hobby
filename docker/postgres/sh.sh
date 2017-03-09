docker run -it --rm --link postgres:postgres \
    postgres psql -U creepy -d creepy -h postgres 