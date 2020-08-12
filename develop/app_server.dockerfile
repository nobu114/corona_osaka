# debian busterベースのpythonイメージを使用 ver3.8.5
FROM python:3.8.5-buster

RUN mkdir -p /app/
WORKDIR /app
