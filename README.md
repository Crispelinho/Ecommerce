# Ecommerce
Esta aplicación permitirá sistematizar los procesos para realizar un flujo de comercio electrónico. La aplicación permitirá administrar los usuarios, productos, pedidos, pagos y envíos. 

## Bases
  Este proyecto fue generado con Python 3.8.5 y Django 3.2.6.

## Instalación para prueba local

### Instalar Python
  - https://www.python.org/downloads/release/python-385/

### Instalar Django
  > ```foo@bar:~$ python -m pip install Django```

### Librerías a instalar
  - pip install django-admin-interface
  - pip install djangorestframework
  - pip install django-bootstrap4
  - pip install django-cors-headers
  - pip install django-import-export
  - pip install django-filter
  - pip install django-rest-multiple-models
  - pip install mysqlclient
  - pip install Pillow
  - pip install djangorestframework-jwt
  - pip install reportlab
  - pip install whitenoise
 
  Nota: Para más información revisar archivo requeriments.txt.
 ## Despliegue Servidor de Desarrollo
  > ```foo@bar:~$ cd ecommerce```
  > 
  > ```foo@bar:~$ python manage.py runserver DEV```

 ## Despliegue Servidor de Producción
  > ```foo@bar:~$ cd ecommerce```
  > 
  > ```foo@bar:~$ python manage.py runserver ```
   
 ## Despliegue Servidor de Producción con Docker
 
 ### Instalar Docker
  -  Descargar e instalar docker: https://docs.docker.com/engine/install/

 ### Instalar Docker Compose
  -  Descargar e instalar docker-compose: https://docs.docker.com/compose/install/

 ### Despliegue del Servidor
  > ```foo@bar:~$ docker-compose build```
  > 
  > ```foo@bar:~$ docker-compose up```

## Aplicación 

### Instalar un administrador de SQLITE
  http://sqliteadmin.orbmu2k.de/
  
### Informe de pedidos pagados y / o enviados
   Con la siguiente consulta podrá obtener en un adminsitrador de SQLITE un informe SQL conla información de los pedidos pagados y / o enviados.
  ```SELECT O.*, CASE WHEN S.STATE_ID ISNULL THEN 0 ELSE S.STATE_ID END AS STATE_SHIP FROM ORDERMANAGEMENT_ORDER AS O
  LEFT JOIN SHIPPINGMANAGEMENT_SHIPMENT AS S ON (O.ID =S.ORDER_ID)
  WHERE O.STATE_ID = 2```
