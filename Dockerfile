FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y nginx

WORKDIR /code/BonApart

COPY requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt

COPY . /code/BonApart

EXPOSE 8000

COPY docker-entrypoint.sh /code/BonApart/docker-entrypoint.sh
RUN chmod +x /code/BonApart/docker-entrypoint.sh

CMD ["/code/BonApart/docker-entrypoint.sh"]
