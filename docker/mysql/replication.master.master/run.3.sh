# find out IP Address of mysql2
mysql2ip=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' mysql2)

# Append the new IP as new host entry in mysql1's host file.
docker exec -i mysql1 sh -c "echo '$mysql2ip mysql2 mysql2' >> /etc/hosts"

# Check if the above command worked
docker exec -i mysql1 sh -c "cat /etc/hosts"