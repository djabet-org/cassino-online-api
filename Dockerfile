FROM python:3.8-alpine
RUN apk update \
    && apk add libpq postgresql-dev \
    && apk add build-base
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["gunicorn", "-b", "0.0.0.0:8080", "--workers", "3", "app:app"]