import os
from typing import Generator
from redis import Redis
from rq import Queue
from .database import SessionLocal

redis = Redis()
if "REDIS_URL" in os.environ:
    redis = Redis.from_url(os.environ.get("REDIS_URL"))

q = Queue(connection=redis)


def get_queue() -> Queue:
    return q


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
