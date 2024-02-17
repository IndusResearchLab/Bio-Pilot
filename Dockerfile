FROM python:3.10-slim-buster

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["sh", "-c", "flask run --host=0.0.0.0 --port=${PORT:-8080}"]

