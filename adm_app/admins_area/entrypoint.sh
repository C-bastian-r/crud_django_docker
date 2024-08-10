#!/bin/sh

# Esperar hasta que PostgreSQL esté disponible
echo "Waiting for PostgreSQL to be available..."
while ! nc -z db 5432; do
  sleep 1
done

# Ejecutar migraciones
echo "Running migrations..."
python manage.py migrate

# Recopilar archivos estáticos sin confirmación
echo "Collecting static files..."
python manage.py collectstatic --noinput


#creando superusuario
python manage.py shell -c "
from django.contrib.auth.models import User
from django.core.management import call_command

username = 'admin'
email = 'admin@example.com'
password = '123456'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print('Superuser created successfully.')
else:
    print('Superuser already exists.')
"

# Iniciar el servidor de aplicación
echo "Starting the application server..."
exec gunicorn -c config/gunicorn/conf.py --bind :8000 admins_area.wsgi:application