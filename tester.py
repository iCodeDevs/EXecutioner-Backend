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
test = TestCase("-12492294823928402840294820482")

job = q.enqueue(tasks.execute,pgm.to_json_object(),test.to_json_object())
time.sleep(1)
test = TestCase.from_json_object(job.result)
print(test.error,test.real_output)