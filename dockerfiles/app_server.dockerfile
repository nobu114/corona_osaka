# debian busterベースのpythonイメージを使用 ver3.8.5
FROM python:3.8.5-slim-buster

RUN mkdir -p /app/config
RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc
RUN apt-get install -y --no-install-recommends libpq-dev
RUN apt-get install -y --no-install-recommends python3-dev
COPY requirements.txt /app/requirements.txt
COPY app/ /app/app/
COPY models/ /app/models/

RUN pip install -r /app/requirements.txt

EXPOSE 9876

WORKDIR /app


ENTRYPOINT ["gunicorn", "-b", ":9876", "app.app:app"]