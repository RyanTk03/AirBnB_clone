#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

echo "Hello World!" > /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]; then
  rm /data/web_static/current
fi
ln -S /data/web_static/releases/test/ /data/web_static/current

echo "server {
  listen 80;
  server_name rayanetoko.tech;

  location /hbnb_static/ {
    alias /data/web_static/current;
    index index.html;
    try_files $uri $uri/ =404;
  }
}" > /etc/nginx/site-available/air_bnb_web_static

ln -S /etc/nginx/site-available/air_bnb_web_static /etc/nginx/site-enabled/air_bnb_web_static

chown ubuntu:ubuntu /data/

service nginx restart