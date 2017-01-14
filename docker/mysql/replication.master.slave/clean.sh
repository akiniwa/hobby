echo 'shutdown master slave'
docker stop master slave
echo 'rm master slave'
docker rm master slave

echo 'rm -rf `pwd`/master/data'
rm -rf `pwd`/master/data
echo 'rm -rf `pwd`/master/log'
rm -rf `pwd`/master/log
echo 'rm -rf `pwd`/slave/data'
rm -rf `pwd`/slave/data
echo 'rm -rf `pwd`/slave/log'
rm -rf `pwd`/slave/log