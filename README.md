# Ecommerce
Esta aplicación permitirá sistematizar los procesos para realizar un flujo de comercio electrónico. La aplicación permitirá administrar los usuarios, productos, pedidos, pagos y envíos. 

## Bases
  Este proyecto fue generado con Python 3.8.5 y Django 3.2.6.

## Instalación para prueba local

### Instalar Python
  - https://www.python.org/downloads/release/python-385/

### Instalar Django
  > ```python -m pip install Django```

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
  > ```console foo@bar:~$ cd ecommerce```
  > python manage.py runserver

 ## Despliegue Servidor de Desarrollo
  > cd ecommerce
  > python manage.py runserver PROD
   
 ### Instalación para prueba con docker
  > docker-compose build
  > docker-compose up
