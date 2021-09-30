### Django REST API для проекта Yatube - соц. сеть для публикации дневников.

>##### Установка
```
 python -m venv venv
 source venv/Scripts/activate
 pip install -r requirements.txt
 python manage.py makemigrations
 python manage.py migrate
 python manage.py createsuperuser
 python manage.py runserver 
```
```
POST http://127.0.0.1:8000/api/v1/token/
```
```
POST http://127.0.0.1:8000/api/v1/posts/
```


>##### Документация проекта:
[http://127.0.0.1:8000/redoc/](http://localhost:8000/redoc/)

>##### Действующий пимер:
[https://asset2.co.vu/redoc/](https://asset2.co.vu/redoc/)

>##### Стек:
```
Python 3, Django REST Framework, PostgreSQL, gunicorn, nginx, Яндекс.Облако(Ubuntu 18.04), pytest, Simple-JWT, GIT
```
>##### Планы по доработке:
```
Запустить в Docker контейнерах nginx, PostgreSQL, Django+gunicorn
```
