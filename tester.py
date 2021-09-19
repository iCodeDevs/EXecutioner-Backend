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
#include<stdio.h>
void main(){
    int num;
    scanf("%d",&num);
    printf("%d",num);
}''',"C")
ev = Evaluation(pgm,[TestCase("12","12"),TestCase("123","123")])
job = q.enqueue(tasks.execute,ev.to_json_object())
time.sleep(15)
print(job.result)