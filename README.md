# client_bot
- Python 3.9.0
- PostgresQL
- [Aiogram](https://docs.aiogram.dev/en/latest/install.html)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)

____

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
