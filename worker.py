from executioner_worker import tasks # preloading
from rq import Connection, Worker

# setup connection (default: localhost:6379/0)
with Connection():
    qs = ['default']

    w = Worker(qs)
    w.work()
