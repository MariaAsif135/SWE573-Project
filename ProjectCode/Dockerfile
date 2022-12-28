# FROM python:3.8

# ENV PYTHONBUFFERED 1

# WORKDIR /django

# ##ADD . /app

# COPY requirements.txt .

# RUN pip install --upgrade pip

# RUN pip install --upgrade setuptools

# RUN pip install ez_setup

# RUN pip install -r requirements.txt

FROM python:3.8

ENV PYTHONBUFFERED 1

WORKDIR /app

##ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install --upgrade setuptools

RUN pip install ez_setup

RUN python -m pip install Pillow

RUN pip install -r requirements.txt


##COPY . /app


##CMD ["python3", "manage.py", "runserver","0.0.0:8000"]