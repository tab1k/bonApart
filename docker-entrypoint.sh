#!/bin/bash

# Запуск Certbot для получения сертификата при первом запуске
certbot certonly --webroot -w /usr/share/nginx/html -d bonapart.kz -d www.bonapart.kz
cp -R /etc/letsencrypt/live/bonapart.kz /etc/nginx/certs


# Запуск Nginx
nginx -g 'daemon off;'


