#!/usr/bin/env bash

python3 init_celery_schedule.py

echo "stop"

celery multi stopwait worker -E -A config --pidfile=/project/notification/worker.pid

echo "start"

celery multi start worker -E -A config -P prefork --concurrency=4 -l info --pidfile=/project/notification/worker.pid --logfile=/project/notification/log/worker.log