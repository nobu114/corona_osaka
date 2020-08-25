FROM python:3.8.5-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY setup_or_update.py setup_or_update.py
COPY models/ models/

ENTRYPOINT ["python","setup_or_update.py"]

