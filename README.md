# lottery
Prueba de django con equipo genesis

docker run --name loteria-mysql -v loteria-db:/var/lib/mysql --network lotteria-net --network-alias mysql -e MYSQL_ROOT_PASSWORD=12345678 -e MYSQL_DATABASE=loteria -e MYSQL_USER=loteria -e MYSQL_PASSWORD=loteria12345678 mysql

