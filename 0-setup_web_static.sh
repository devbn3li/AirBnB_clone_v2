#!/usr/bin/env bash
# Sets up my web servers for the deployment of web_static

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
sudo sh -c 'echo "Mohamed Ezzat @ Holberton School" > /data/web_static/releases/test/index.html'

# Create or recreate the symbolic link
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sh -c 'echo "server {
    listen 80;
    listen [::]:80 default_server;
    server_name mohamedezzat.tech;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}" > /etc/nginx/sites-available/default'

# Restart Nginx
sudo service nginx restart
