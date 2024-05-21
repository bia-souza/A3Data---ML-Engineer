FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/app/src"

WORKDIR /app/src/iris-pipeline

CMD ["kedro", "run"]
