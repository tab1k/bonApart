#!/bin/bash

# Запуск Certbot для получения сертификата при первом запуске
certbot certonly --webroot -w /usr/share/nginx/html -d your_domain.com -d www.your_domain.com

# Копирование сертификатов в папку Nginx
cp -R /etc/letsencrypt/live/your_domain.com /etc/nginx/certs

# Запуск Nginx
nginx -g 'daemon off;'
