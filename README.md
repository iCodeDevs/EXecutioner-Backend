# EXecutioner-worker

A worker process to execute code

## Installation

- Install [Poetry](https://python-poetry.org/docs/)

- Install dependencies

    ```bash
    poetry install
    ```

- Install [Executioner](https://github.com/iCodeDevs/EXecutioner) dependencies (if being used as worker)

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
from executioner_worker import tasks
from executioner.program import Program
from executioner.evaluate import Evaluation, TestCase
from redis import Redis
from rq import Queue
import time

# default is localhost:6379
# be sure to start a redis instance and worker process before trying this out
conn = Redis(db=0) 
q = Queue(connection=conn)
pgm = Program("print('h')","python3")
ev = Evaluation(pgm,[TestCase("",""),TestCase("h","he")])
job = q.enqueue(tasks.execute,ev.to_json_object())
time.sleep(5)
print(job.result)
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

## NOTES

### To apply .env in bash

```bash
set -o allexport; source .env; set +o allexport
```
