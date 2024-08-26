FROM python:3.10-alpine

# Встановимо змінну середовища
ENV APP_ROOT=/app

# Встановимо робочу директорію всередині контейнера
WORKDIR $APP_ROOT

COPY . .

# Installing client libraries and any other package you need
RUN apk update && apk add --no-cache bash

# To run w/ requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]