import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


def check_celery_works() -> bool:
    try:
        insp = app.control.inspect()
        d = insp.stats()
        if not d:
            return False
        else:
            return True
    except Exception as e:
        return False
