# client_bot
- Python 3.9.0
- PostgresQL
- [Aiogram](https://docs.aiogram.dev/en/latest/install.html)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)

____
### Запуск (Ubuntu)
1. Установите docker, docker-compose, git.<br>
2. Склонируйте проект из github. 
```sh
git clone https://github.com/tinkml/client_bot.git
```
3. Зайдите в папку с проектом,
   скопируйте переменные из *.env.example в .env и укажите недостающие.
```sh
cd client_bot/
cat env.example > .env
```
4. Запустите процесс сбоки контейнеров с помощью docker-compose.
```sh
docker-compose up -d --build postgres
sudo docker-compose up -d --build bot
```

### Alembic миграции
Для миграций используется библиотека alembic.
[Документация](https://alembic.sqlalchemy.org/en/latest/index.html)
<br>
При первом запуске, необходимо инициализировать alembic:
```sh
alembic init --template async 'Название директории'
```
После инициализации требуется настроить файл env.py в созданной директории.<br>
После чего можем создать миграции:
```
1. alembic revision --autogenerate -m 'Название коммита'
2. alembic upgrade head
```
