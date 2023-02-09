sudo -u postgres psql

CREATE DATABASE easycrmdb;

CREATE USER easyuser WITH PASSWORD 'easy@123';
ALTER ROLE easyuser SET client_encoding TO 'utf8';
ALTER ROLE easyuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE easyuser SET timezone TO 'UTC';
\q

server {
    listen 80;
    server_name 13.233.59.57;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/crm;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}


sudo ln -s /etc/nginx/sites-available/crm /etc/nginx/sites-enabled


[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=//home/ubuntu/crm
ExecStart=//home/ubuntu/crm/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          config.wsgi:application

[Install]
WantedBy=multi-user.target






sudo systemctl daemon-reload
sudo systemctl restart gunicorn.socket gunicorn.service

sudo nginx -t && sudo systemctl restart nginx