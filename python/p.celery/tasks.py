# -*- coding: utf-8 -*-

from celery import Celery

app = Celery(
    'tasks',
    backend='redis://192.168.99.100:6379/0',
    broker='redis://192.168.99.100:6379/0',
)

app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
)


@app.task
def add(x, y):
    """add"""
    return x + y
