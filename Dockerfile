FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y --no-install-recommends gdal-bin
RUN apt-get install -y mime-support
WORKDIR /code/bonapart

COPY requirements.txt /code/requirements.txt
RUN pip3 install --upgrade pip
RUN pip install -r /code/requirements.txt
RUN pip3 install Pillow psycopg2

COPY . /code/bonapart

EXPOSE 8000

COPY ./docker-entrypoint.sh /code/bonapart/docker-entrypoint.sh

RUN chmod +x /code/bonapart/docker-entrypoint.sh

CMD ["/code/bonapart/docker-entrypoint.sh"]