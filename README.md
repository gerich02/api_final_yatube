# YatubeAPI
API проекта для размещения блогов. 

## Содержание
- [Описание](#описание)
- [Стек технологий](#cтек-технологий)
- [Запуск проекта](#запуск-проекта)
- [Примеры запросов API](#примеры-запросов-api)
- [Автор проекта](#автор-проекта)

## Описание
Данное API позволяет получать информацию о постах, комментариях, группах и подписках с сервиса "Yatube".

## Стек технологий
Python 3.11.3,
Django 3.2.16,
Django Rest Framework,
Djoser + JWT

## Запуск проекта
Клонировать репозиторий и перейти в него через терминал:

```
git clone https://github.com/OlejkaS/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:


```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Примеры запросов и ответов API

### GET-запрос на получение постов:
```
api/v1/posts/
```
### Ответ от API:
```
[
    {
        "id": 1,
        "author": "George",
        "text": "hello",
        "pub_date": "2023-18-10T12:09:25.330391Z",
        "image": null,
        "group": null
    }
]
```

### GET-запрос на получение информации о конкретном посте по ID:
```
api/v1/posts/{id}/
```
### Ответ от API:
```
{
    "id": 1,
    "author": "George",
    "text": "hello",
    "pub_date": "2023-10-10T12:09:25.330391Z",
    "image": null,
    "group": null
}
```

### GET-запрос на получение комментариев к постам:
```
api/v1/posts/{post_id}/comments/
```
### Ответ от API:
```
[
    {
        "id": 1,
        "post": 1,
        "author": "George",
        "text": "Best of the best",
        "created": "2023-18-10T12:11:55.905999Z"
    }
]
```

### GET-запрос на получение информации о группе:
```
api/v1/groups/{id}/
```
### Ответ от API:
```
[
    {
        "id": 1,
        "title": "Группа",
        "slug": "group_1",
        "description": "Описание"
    }
]
```

### POST-запрос для подписки на пользователя:
```
api/v1/follow/
```
### Ответ от API:
```
{
    "id": 1,
    "user": "George",
    "following": "Galina"
}
```

## Автор проекта

- [Варивода Георгий](https://github.com/gerich02)