FROM python:3.9-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
