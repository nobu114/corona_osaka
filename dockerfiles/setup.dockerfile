FROM python:3.8.5-buster

RUN mkdir -p /app/
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY setup_or_update.py /app/setup_or_update.py
WORKDIR /app
CMD ["python","setup_or_update.py"]

