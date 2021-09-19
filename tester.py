from executioner_worker import tasks
from executioner.program import Program
from executioner.evaluate import Evaluation, TestCase
from redis import Redis
from rq import Queue
import time

conn = Redis(db=0)
q = Queue(connection=conn)
pgm = Program("print('h')","python3")
ev = Evaluation(pgm,[TestCase("",""),TestCase("h","he")])
job = q.enqueue(tasks.execute,ev.to_json_object())
time.sleep(5)
print(job.result)