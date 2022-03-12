API YaMDb (проект в Docker-контейнерах)
![example workflow](https://github.com/NikitaChalykh/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
=====

Описание проекта
----------
Проект YaMDb собирает отзывы пользователей на произведения (книги, фильмы и музыка). Произведению может быть присвоен жанр из списка предустановленных.
Новые жанры может создавать только администратор.
Пользователи оставляют к произведениям текстовые отзывы
и ставят произведению оценку в диапазоне от одного до десяти (целое число). На основании оценок рассчитывается общий рейтинг произведения.
На одно произведение пользователь может оставить только один отзыв.

Реализован REST API CRUD для моделей проекта, для аутентификации примненяется JWT-токен.
В проекте реализованы пермишены, фильтрации, сортировки и поиск по запросам клиентов, реализована пагинация ответов от API, установлено ограничение количества запросов к API.

Системные требования
----------
* Python 3.6+
* Docker
* Works on Linux, Windows, macOS, BS

Стек технологий
----------
* Python 3.8
* Django 2.2
* Django Rest Framework
* Simple-JWT
* PostreSQL
* Nginx
* gunicorn
* Docker
* GitHub Actions (CI/CD)

Установка проекта из репозитория
----------
1. Клонировать репозиторий и перейти в него в командной строке:
```bash 
git clone 'https://github.com/NikitaChalykh/infra_sp2.git'

cd yamdb_final
```

2. Cоздать и открыть файл ```.env``` с переменными окружения:
```bash 
cd infra

nano .env
```

3. Заполнить ```.env``` файл с переменными окружения по примеру:
```bash 
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres 
POSTGRES_USER=postgres 
POSTGRES_PASSWORD=postgres
DB_HOST=db 
DB_PORT=5432 
SECRET_KEY=p&l%385148kslhtyn^##a1)ilz@4zqj=rq&agdol^##zgl9(vs
```

4. Установка b запуск приложения в контейнерах (контейнер web загружактся из DockerHub):
```bash 
docker-compose up -d
```

5. Запуск миграций, создание суперюзера, сбор статики и заполнение БД:
```bash 
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser

docker-compose exec web python manage.py collectstatic --no-input 

docker-compose exec web python manage.py loaddata fixtures.json
```

Документация
----------
Документация для API [доступна по ссылке](http://localhost/redoc/) после установки приложения.
