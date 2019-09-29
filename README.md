# project11
Тестовое задание

1. Установка
docker-compose up
docker-compose web python3 manage.py makemigrations
# сами миграции начинаются автоматически по docker-compose up, но если очень нужно то:
docker-compose web python3 manage.py migrate

2. Наполнение данными
docker-compose web python3 manage.py loaddata dump.json

3.Тесты
docker-compose web python3 manage.py test
2 теста на ответ 200 от двух роутов

4. Примеры зыпросов:
http://127.0.0.1:8000/api/page/2
где 2 id страницы

http://127.0.0.1:8000/api/pages/0/10/
где 0 оффсет, 10 лимит
