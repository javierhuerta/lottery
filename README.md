# lottery
Prueba de django con equipo genesis


## Comando de docker para ejecutar contenedor de aplicacion django en un network especifico y con sincronizacion en tiempo real del codigo fuente

docker run -dp 8000:8000 --name loteria-app --network loteria-net -w /code --mount type=bind,src="$(pwd)",target=/code python:3.10.4 sh -c "pip install -r requirements.txt && python manage.py migrate && python manage.py runserver 0.0.0.0:8000" 


## Comando de docker para ejecutar base de datos mysql con persistencia de datos y en un network especifico agregando un alias para el contendor

docker run -d --name loteria-db -v loteria-db:/var/lib/mysql --network loteria-net --network-alias mysql -e MYSQL_ROOT_PASSWORD=12345678 -e MYSQL_DATABASE=loteria -e MYSQL_USER=loteria -e MYSQL_PASSWORD=loteria12345678 mysql

