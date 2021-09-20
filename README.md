# EXecutioner-worker

A worker process to execute code

## Installation

- Install [Poetry](https://python-poetry.org/docs/)

- Install dependencies

  ```bash
  poetry install
  ```

- Install [Executioner](https://github.com/iCodeDevs/EXecutioner) dependencies (if being used as worker)

## Configuration

- create a .env file

  - Redis URL format in .env

  ```bash
  REDIS_URL=redis://[[USER]:PASSWORD@]HOST[:PORT][/DATABASE]
  ```

- apply .env in bash

  ```bash
  set -o allexport; source .env; set +o allexport
  ```

## How To Use

### As worker

Use the library as a worker process across multiple systems connected to a single redis instance. The redis connection can be configured in worker.py.

To start the worker process

```bash
poetry run python worker.py
```

### As client

Import executioner_worker.tasks and enqueue as task to execute it (example given in tester.py)

```python
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
test = TestCase("12")
job = q.enqueue(tasks.execute,pgm.to_json_object(),test.to_json_object())
time.sleep(10)
test = TestCase.from_json_object(job.result)
print(test.real_output)
```

### Development

Use [docker-compose](https://docs.docker.com/compose/install/) to start a redis instance

```bash
docker-compose up -d
```

To shut the instance down

```bash
docker-compose down
```
