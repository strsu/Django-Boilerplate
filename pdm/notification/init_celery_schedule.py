import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.settings")

import django

django.setup()  # 장고 프로젝트 셋업

from django_celery_beat.models import PeriodicTask

PeriodicTask.objects.update(last_run_at=None)
