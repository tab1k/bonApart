#!/bin/bash
set -e

# Ждем запуска PostgreSQL
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "db" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  >&2 echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "PostgreSQL is up - continuing with Django entrypoint"

# Применяем миграции
python manage.py migrate
python manage.py collectstatic

# Запускаем сервер
exec "$@"
