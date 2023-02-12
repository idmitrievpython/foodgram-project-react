# Проект "Продуктовый помощник". FoodGramm

## Описание
http://158.160.24.84/api
http://158.160.24.84/admin (логин: admin, пароль: admin)
Cервис позволяет пользователям публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Шаблон заполнения .env файла
```bash
DB_ENGINE=<тип БД>
DB_NAME=<имя базы данных>
POSTGRES_USER=<логин для подключения к базе данных>
POSTGRES_PASSWORD=<пароль для подключения к БД>
DB_HOST=<название сервиса (контейнера)>
DB_PORT=<порт для подключения к БД>
SECRET_KEY=<SECRET_KEY Django>
```
## Установка
- Склонировать репозиторий
```bash
git clone https://github.com/idmitrievpython/foodgram-project-react.git
```
- Запустить проект в контейнерах Docker
```bash
cd infra
docker-compose up -d
```
- Провести миграции:
```bash
docker-compose exec backend python manage.py migrate
```
- Создать суперпользователя:
```bash
docker-compose exec backend python manage.py createsuperuser
```
- Собрать статику:
```bash
docker-compose exec backend python manage.py collectstatic --no-input
```
## Автор проекта
Дмитриев Илья студент 15 кагорты ЯндексПрактикум