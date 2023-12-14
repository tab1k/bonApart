FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установка необходимых зависимостей
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gdal-bin \
        mime-support \
        libgdal-dev

# Установка Python-зависимостей
WORKDIR /code/BonApart
COPY requirements.txt /code/requirements.txt
RUN pip3 install --upgrade pip
RUN pip install -r /code/requirements.txt
RUN pip3 install Pillow psycopg2

# Копирование остальных файлов
COPY . /code/BonApart

# Настройка точки входа
COPY ./docker-entrypoint.sh ./docker-entrypoint.sh
RUN chmod +x /code/BonApart/docker-entrypoint.sh

# Определение команды для запуска контейнера
CMD ["/code/BonApart/docker-entrypoint.sh"]

