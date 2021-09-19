import os
from executioner_worker import tasks
from executioner.program import Program
from executioner.evaluate import Evaluation, TestCase
from redis import Redis
from rq import Queue
import time

redis = None
if "REDIS_URL" in os.environ:
    redis = Redis.from_url(os.environ.get("REDIS_URL"))

q = Queue(connection=redis)
pgm = Program('''
a = 0
for _ in range(10**9):
    a +=1
''',"python3")
ev = Evaluation(pgm,[TestCase("",""),TestCase("h","he")])
job = q.enqueue(tasks.execute,ev.to_json_object())
time.sleep(60)
print(job.result)