FROM python:3

RUN apt-get update

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /static /media

COPY requirements.txt /code/requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install Pillow psycopg2


COPY . /code
COPY ./docker-entrypoint.sh ./docker-entrypoint.sh

# Set docker-entrypoint
RUN chmod +x /code/docker-entrypoint.sh
CMD ["/code/docker-entrypoint.sh"]