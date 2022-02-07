# Python3-http-boilerplate
Simple boilerplate for http python3 CRUD service

## Set env file
```
$ cp .env.example ./app/env
```

#### Edit .env

```
$ vim ./app/.env
```

```
ENV=local
PREFIX=boilerplate

PORT=3050
LOGGING_LEVEL=DEBUG
SERVICE_NAME=boilerplate
```
## Local dependencies
```
$ pip3 install --no-cache-dir -r ./app/requirements.txt
```

## Run local
```
python3 -m app
```

## Build Docker
```
docker-compose --env-file ./app/.env build --no-cache
```

## Run Docker
```
docker-compose --env-file ./app/.env up --build
```
