# Используем базовый образ с поддержкой Python
FROM python:3

# Устанавливаем переменную окружения для предотвращения вывода сообщений от Python
ENV PYTHONDONTWRITEBYTECODE 1

# Отключаем буферизацию вывода стандартного потока ввода/вывода/ошибок
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию в /code
WORKDIR /code

# Копируем requirements.txt внутрь контейнера
COPY requirements.txt /code/

# Обновляем pip и устанавливаем зависимости
RUN pip install --upgrade pip && pip install -r requirements.txt

# Создаем директории для статических и медиа файлов
RUN mkdir -p /code/static /code/media

# Копируем все файлы из текущего каталога в /code внутри контейнера
COPY . /code

# Копируем файл proxy_params внутрь контейнера
COPY nginx/proxy_params /code/nginx/proxy_params

# EXPOSE необходим, если вы хотите открыть порт из контейнера
EXPOSE 8000

# Команда для запуска приложения
CMD ["./docker-entrypoint.sh"]


