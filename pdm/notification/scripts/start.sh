#!/usr/bin/env bash

mkdir -p log

sleep 5; # wait for the database to be ready

python manage.py migrate
python manage.py collectstatic --noinput --verbosity 0

if [ "$WHOAMI" = "local" ]; then
    python manage.py runserver 0.0.0.0:8000
else
    gunicorn -c config/gunicorn.conf.py config.asgi:application
fi