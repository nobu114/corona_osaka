# debian busterベースのpythonイメージを使用 ver3.8.5
FROM python:3.8.5-slim-buster

RUN mkdir -p /app/config
COPY requirements.txt /app/requirements.txt
