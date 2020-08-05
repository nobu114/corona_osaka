# debian busterベースのpythonイメージを使用 ver3.8.5
FROM python:3.8.5-slim-buster

RUN mkdir -p /app/config
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ESXPOSE 9876

WORKDIR /app


ENTRYPOINT ["gunicorn", "flask_app:app"]