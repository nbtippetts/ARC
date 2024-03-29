
FROM python:3
ENV PYTHONUNBUFFERED 1
ENV REDIS_HOST "redis"
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput