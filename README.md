# EXecutioner-Backend

Backend for executioner

## Installation

- Install [Poetry](https://python-poetry.org/docs/)

- Install dependencies

  ```bash
  poetry install
  ```

- Install [Executioner](https://github.com/iCodeDevs/EXecutioner) dependencies (if being used as worker)

## Configuration

- create a .env file

  ```bash
  REDIS_URL=redis://[[USER]:PASSWORD@]HOST[:PORT][/DATABASE]
  ```

- apply .env in bash

  ```bash
  set -o allexport; source .env; set +o allexport
  ```

- apply migrations

  ```bash
  poetry run alembic upgrade head
  ```

## Components

### Worker

The worker process handles tasks from redis and returns their result after execution.

To start the worker

```bash
poetry run python3 worker.py
```

### Web server

The web server provides the web API

To start the web server

```bash
poetry run uvicorn app.main:app --reload
```

## Development

Use [docker-compose](https://docs.docker.com/compose/install/) to start a redis instance

```bash
docker-compose up -d
```

To shut the instance down

```bash
docker-compose down
```
