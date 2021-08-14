# pull official base image
FROM python:3.8.5

# set work directory
RUN mkdir /code
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get install -y \
    postgresql \
    postgresql-server-dev-all \
    gcc \
    python3-dev \
    musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./merlin/entrypoint.sh .

# copy project
COPY . /code/

# ENTRYPOINT [":/code/entrypoint.sh"]
