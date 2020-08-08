# debian busterベースのpythonイメージを使用 ver3.8.5
FROM python:3.8.5-slim-buster

RUN mkdir -p /app/config
RUN apt update
RUN apt install -y gcc
RUN apt install -y libpq-dev 
COPY requirements.txt /app/requirements.txt
COPY app/ /app/app/
COPY models/ /app/models/

RUN pip install -r /app/requirements.txt

EXPOSE 9876

WORKDIR /app


ENTRYPOINT ["gunicorn", "app.app:app"]