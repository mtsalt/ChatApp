FROM python:alpine

WORKDIR /app

COPY ./app /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "server.py"]