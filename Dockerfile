FROM python:3.8-alpine
RUN apk update \
    && apk add libpq postgresql-dev \
    && apk add build-base
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
# CMD ["python", "src/ws_blaze_crash.py"]