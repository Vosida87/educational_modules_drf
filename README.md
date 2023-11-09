# educational_modules_drf
Проект по взаимодействию с образовательными модулями, идентификатор ТЗ - TB2, стек технологий: Django, DRF, Djoser, PostgreSQL, Docker.

## Данные для .env файла  
#### Информация для доступа к базе данных  
DB_ENGINE='django.db.backends.postgresql' (если postgresql)  
DB_NAME='имя_базы_даных'  
DB_USER='postgres'  
DB_PASSWORD='пароль'  
HOST='localhost'  
#### django secret key  
SECRET_KEY='ваш_ключ_джанго'  

## Установка зависимостей  
`pip install -r requirements`  

## Создание суперпользователя для использования админки
`python manage.py createsuperuser`  

## Миграции
`python manage.py makemigrations`  
`python manage.py migrate`  

## Проверка покрытия тестами
`coverage run manage.py test`  
`coverage report`  
Для более подробного отчёта `coverage annotate`  

## запуск docker  
Запуск контейнеров: `docker-compose up`  
Миграция: `docker-compose exec web python manage.py migrate`  
Остановить и удалить контейнеры: `docker-compose down`  

### Требования по тз
* PostgreSQL - выполнено;
* ORM - используется django;
* MVC/MTV - использована Model-View-Controller;
* FBV/CBV - использовано Class-Based Views;
* serializers - есть;
* viewset/generic - использован generic;
* Tests - покрытие 98%;
* Git - есть коммиты;
* Readme - есть;
* PEP8 - соблюдён;
* Swagger - есть `http://127.0.0.1:8000/redoc/`.
