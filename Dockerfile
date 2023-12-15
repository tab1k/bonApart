FROM python:3.8

# Добавьте эти строки в начало Dockerfile
ARG http_proxy
ARG https_proxy

ENV http_proxy ${http_proxy}
ENV https_proxy ${https_proxy}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установка необходимых пакетов для Certbot
RUN apt-get update && apt-get install -y software-properties-common \
    && add-apt-repository -y ppa:certbot/certbot \
    && apt-get update \
    && apt-get install -y certbot netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install --upgrade pip \
    && pip install -r /code/requirements.txt \
    && pip install Pillow psycopg2

COPY . /code
COPY docker-entrypoint.sh /code/docker-entrypoint.sh
RUN chmod +x /code/docker-entrypoint.sh

CMD ["/code/docker-entrypoint.sh"]
