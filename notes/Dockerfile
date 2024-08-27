FROM python:3.10-alpine

# Встановимо змінну середовища
ENV APP_ROOT=/app

# Встановимо робочу директорію всередині контейнера
WORKDIR $APP_ROOT

COPY . .

# Installing client libraries and any other package you need
RUN apk update && apk add --no-cache bash && apk add --no-cache libpq

RUN apk add --no-cache --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev


# To run w/ requirements.txt
RUN pip3 install -r requirements.txt

# Delete build dependencies
RUN apk del build-deps gcc

# Ensure the script is executable
RUN chmod +x runme.sh

EXPOSE 8000

CMD ["./runme.sh"]