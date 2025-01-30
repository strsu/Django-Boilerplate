#!/usr/bin/env bash

echo "stop"

celery multi stopwait worker -E -A config --pidfile=/project/notification/worker.pid