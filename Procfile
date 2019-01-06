release: heroku run python manage.py migrate
release: heroku run python manage.py createsuperuser
web: gunicorn site_assinaki.wsgi --log-file -
