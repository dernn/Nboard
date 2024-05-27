import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmorpg.settings')

app = Celery('mmorpg')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# для запуска воркера/периодических задач [в разных окнах терминала]:
# redis-server.exe [от имени администратора]
# python manage.py runserver
# celery -A <project_name> worker -l INFO --pool=solo
# celery -A <project_name> beat -l INFO

app.conf.beat_schedule = {
    'mailing_every_monday_8am': {
        'task': 'mailing.tasks.celery_weekly_mailing',
        # рассылка каждый понедельник в 8.00 UTC [TIME_ZONE from settings]
        'schedule': crontab(minute=0, hour=8, day_of_week='mon'),
        'args': (),
    },
}
