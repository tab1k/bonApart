#!/bin/sh
# docker-entrypoint.sh

# Ожидаем доступности PostgreSQL
echo "Ждем запуска PostgreSQL..."
while ! nc -z db 5432; do
  sleep 1
done
echo "PostgreSQL запущен. Продолжаем..."

# Применяем миграции
python manage.py migrate

# Собираем статику
python manage.py collectstatic --noinput

# Запускаем сервер
exec "$@"
