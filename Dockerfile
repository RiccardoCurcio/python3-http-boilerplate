FROM python:3

WORKDIR /usr/src/service

RUN mkdir /usr/src/service/app

COPY ./app ./app

RUN apt-get -y update

RUN apt-get -y install libssl-dev libffi-dev python3-openssl

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r ./app/requirements.txt

CMD [ "python", "-m", "app" ]
