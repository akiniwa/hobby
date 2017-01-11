echo 'shutdown mysql1 mysql2'
docker stop mysql1 mysql2
echo 'rm mysql1 mysql2'
docker rm mysql1 mysql2

echo 'rm -rf `pwd`/master1/data'
rm -rf `pwd`/master1/data
echo 'rm -rf `pwd`/master1/log'
rm -rf `pwd`/master1/log
echo 'rm -rf `pwd`/master2/data'
rm -rf `pwd`/master2/data
echo 'rm -rf `pwd`/master2/log'
rm -rf `pwd`/master2/log