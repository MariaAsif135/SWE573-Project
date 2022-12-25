FROM python:3.8

ENV PYTHONBUFFERED 1

WORKDIR /django

##ADD . /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --upgrade setuptools

RUN pip install ez_setup

RUN pip install -r requirements.txt