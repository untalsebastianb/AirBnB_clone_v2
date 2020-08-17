#!/usr/bin/env bash
# Configure server with static pages
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "Holberton School" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current 
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server;/a location /hbnb_static {alias data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
