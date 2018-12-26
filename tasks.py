from celery import Celery 
from ddtrace import patch

patch(celery=True)

app = Celery('tasks', broker='amqp://localhost')

@app.task
def add(x, y):
    return x + y
