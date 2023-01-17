##sudo lsof -t -i tcp:8000 | xargs kill -9


 docker-compose -f local.yml run --rm django python manage.py createsuperuser
  docker-compose -f local.yml run --rm django python manage.py makemigrations
   docker-compose -f local.yml run --rm django python manage.py migrate
    docker-compose -f local.yml up
docker-compose -f local.yml up
docker-compose -f local.yml down
