release: python manage.py migrate
release: python manage.py createsuperuser
web: gunicorn site_assinaki.wsgi --log-file -
