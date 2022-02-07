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


## Requests

#### healthcheck
```
GET http://localhost:3050/healthcheck
```

#### read all
```
GET http://localhost:3050/v1/companies
```

#### read single item
```
GET http://localhost:3050/v1/companies/{id}
```

#### crete new item
``` 
POST http://localhost:3050/v1/companies

header

    Content-Type: application/json

body: 

    {
    	"name": "test",
    	"iban": "iban",
    	"email": "company@email.com"
    }
```

#### update sigle item
```
PUT http://localhost:3050/v1/companies/{id}

header

    Content-Type: application/json

body: 

    {
    	"name": "test",
    	"iban": "iban",
    	"email": "company@email.com"
    }
```

### delete sigle item
```
DELETE http://localhost:3050/v1/companies/{id}
```