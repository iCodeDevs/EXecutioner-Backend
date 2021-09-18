from celery import Celery

app = Celery('executioner_worker',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/1',
             include=['executioner_worker.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()