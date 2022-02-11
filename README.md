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
ENV=local
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


## Requests example

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