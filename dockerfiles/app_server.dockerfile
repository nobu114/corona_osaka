# debian busterベースのpythonイメージを使用 ver3.8.5
FROM python:3.8.5-buster

RUN mkdir -p /app/config
COPY requirements.txt /app/requirements.txt
COPY app/ /app/app/
COPY models/ /app/models/
# COPY setup_or_update.py /app/setup_or_update.py

RUN pip install -r /app/requirements.txt

EXPOSE 9876

WORKDIR /app

# RUN python3 setup_or_update.py

ENTRYPOINT ["gunicorn", "-b", ":9876", "app.app:app"]