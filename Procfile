web: gunicorn  hotel_management.wsgi:application --log-file -
python3 manage.py collectstatic --noinput
manage.py migrate