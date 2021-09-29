import os
from executioner_worker import tasks
from executioner.program import Program
from executioner.evaluate import Evaluation, TestCase
from redis import Redis
from rq import Queue
import time

redis = Redis()
if "REDIS_URL" in os.environ:
    redis = Redis.from_url(os.environ.get("REDIS_URL"))

q = Queue(connection=redis)
pgm = Program('''
print("hello world")
''',"python3")
test = TestCase()

job = q.enqueue(tasks.execute,pgm.to_json_object(),test.to_json_object())
time.sleep(1)
print(job.result)
test = TestCase.from_json_object(job.result)
print(test.error,test.real_output)