import os
from executioner_worker import tasks # preloading
from rq import Connection, Worker
from redis import Redis

redis = None
if "REDIS_URL" in os.environ:
    redis = Redis.from_url(os.environ.get("REDIS_URL"))

with Connection(redis):
    qs = ['default']

    w = Worker(qs)
    w.work()
