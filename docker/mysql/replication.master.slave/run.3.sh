echo "step 6 create table in mysql master"
docker exec -ti master mysql -uroot -pcreepy -e \
	"create table creepy.students(id int, name varchar(20));" \
	-vvv
echo "---> check table in mysql master's creepy database"
docker exec -ti slave mysql -uroot -pcreepy -e \
	"show tables in creepy;" \
	-vvv
echo "---> check table in mysql slave's creepy database"
docker exec -ti slave mysql -uroot -pcreepy -e \
	"show tables in creepy;" \
	-vvv

echo "step 7 insert into mysql master's creepy database"
docker exec -ti master mysql -uroot -pcreepy -e \
	"insert into creepy.students values (1, 'gree2');" \
	-vvv
echo "---> check table in mysql master's creepy database"
docker exec -ti master mysql -uroot -pcreepy -e \
	"select * from creepy.students;" \
	-vvv
echo "---> check table in mysql slave's creepy database"
docker exec -ti slave mysql -uroot -pcreepy -e \
	"select * from creepy.students;" \
	-vvv
