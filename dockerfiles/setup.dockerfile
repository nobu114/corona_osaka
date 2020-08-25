FROM python:3.8.5-buster

RUN mkdir -p /app
COPY requirements.txt /app/requirements.txt
COPY setup_or_update.py /app/setup_or_update.py
COPY models/ /app/models/
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python","setup_or_update.py"]

