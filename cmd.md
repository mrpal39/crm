## sudo lsof -t -i tcp:8000 | xargs kill -9


### docker-compose -f local.yml run --rm django python manage.py createsuperuser
### docker-compose -f local.yml run --rm django python manage.py makemigrations
### docker-compose -f local.yml run --rm django python manage.py migrate
### docker-compose -f local.yml up
### docker-compose -f local.yml up
### docker-compose -f local.yml down

# docker-compose -f local.yml build

# $ export DATABASE_URL=postgres://rahulpal:rahul@123@127.0.0.1:5432/cmsScraper
# Optional: set broker URL if using Celery
# $ export CELERY_BROKER_URL=redis://localhost:6379/0
 export DATABASE_URL=postgres://rahulpal:rahul@123@127.0.0.1:5432/cmsScraper
 export CELERY_BROKER_URL=redis://localhost:6379/0
