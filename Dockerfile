FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN echo "deb http://deb.debian.org/debian buster main" >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y --no-install-recommends gdal-bin
RUN apt-get install -y mime-support
WORKDIR /code/BonApart

COPY requirements.txt /code/requirements.txt
RUN pip3 install --upgrade pip
RUN pip install -r /code/requirements.txt
RUN pip3 install Pillow psycopg2

COPY . /code/BonApart

EXPOSE 8000

COPY . /code/BonApart
COPY ./docker-entrypoint.sh ./docker-entrypoint.sh


RUN chmod +x /code/BonApart/docker-entrypoint.sh
CMD ["/code/BonApart/docker-entrypoint.sh"]

