FROM python:3.8-alpine3.16
LABEL maintainer="niknik3000"

ENV LANG=ru_RU.utf8
RUN mkdir -p /usr/src/app/token/
WORKDIR /usr/src/app/
COPY ./requirements.txt /usr/src/app/
RUN apk add --no-cache build-base libffi-dev && pip3 install --no-cache-dir -r requirements.txt