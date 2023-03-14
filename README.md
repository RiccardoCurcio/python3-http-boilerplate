# Python3-http-boilerplate
Simple boilerplate for http python3 CRUD service

## Featue
* Resolve corss-origin
* async processes for generete separated actions *Ex. send email without wait the response from an external service sevice*

## Set env file
```
$ cp .env.example .env
```

#### Edit .env

```
$ vim .env
```

```
ENV=local #local #dev #prod #test
PREFIX=boilerplate

PORT=3050
LOGGING_LEVEL=DEBUG
SERVICE_NAME=boilerplate


# CORSS_ORIGIN
CORSS_ORIGIN_RESOLVE=true
ALLOW_CREDENTIALS=true
ALLOW_ORIGIN=https://py3-http-boilerplate.local
ALLOW_METHODS=POST, GET, PUT, PATCH, DELETE, OPTIONS
ALLOW_HEADERS=Content-Type
MAX_AGE=86400
VARY=Origin
CACHE_CONTROLL=private, must-revalidate

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
docker-compose build --no-cache
```

## Run Docker
```
docker-compose up --build
```

## Run Test
```
python3 -m app ENV=test

pytest
```


## Requests example

#### healthcheck
```
GET http://localhost:3050/healthcheck
```

#### read all
```
GET http://localhost:3050/v1/placeholders
```

#### read single item
```
GET http://localhost:3050/v1/placeholders/{id}
```

#### crete new item
``` 
POST http://localhost:3050/v1/placeholders

header

    Content-Type: application/json

body: 

    {
        "name": "tss",
        "vatNumber": "000000",
        "phones": ["3492256745", "0039 (333) 3423456", "+23 435 7865345"],
        "emails": ["ere@pino.com"]
    }
```

#### update sigle item
```
PUT http://localhost:3050/v1/placeholders/{id}

header

    Content-Type: application/json

body: 

    {
        "name": "tss",
        "vatNumber": "000000",
        "phones": [],
        "emails": []
    }
```

### delete sigle item
```
DELETE http://localhost:3050/v1/placeholders/{id}
```