#!/usr/bin/env bash

sleep 5; # wait for the database to be ready

rm -f /project/notification/worker.pid

python3 init_celery_schedule.py

celery multi start worker -E -A config -P prefork --concurrency=4 -l info --pidfile=/project/notification/worker.pid --logfile=/project/notification/log/worker.log

celery -A config beat -l info