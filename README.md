# dogger_backend_demo

Backend Dogger Demo

Para levantar el proyecto.
 
 Instalar dependencias:

- pip install -r requeriments.txt

- Crear un .env, copiandolo de .env.example

En el .env, ingresar las credenciales de la base de datos. Se trabajó con Postgresql.

Correr los siguientes comandos para crear la estructura de la DB
- python manage.py makemigrations
- python manage.py migrate


Correr los Seeders en el siguiente orden:

python3 manage.py loaddata user
python3 manage.py loaddata dogsize
python3 manage.py loaddata person
python3 manage.py loaddata dogs
python3 manage.py loaddata profiles
python3 manage.py loaddata walker
python3 manage.py loaddata walkerxdog
python3 manage.py loaddata profileuser
python3 manage.py loaddata eventcalendar

Finalmente, iniciar el proyecto con:
- python manage.py runserver



