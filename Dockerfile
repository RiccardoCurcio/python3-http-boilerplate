FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN apt-get -y update

RUN apt-get -y install libssl-dev libffi-dev python3-openssl

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]
