# Cat Charity Fund API

FastAPI-приложение для благотворительного фонда QRKot. Позволяет:
- управлять проектами фонда (CRUD для суперпользователей, чтение — всем);
- принимать пожертвования от зарегистрированных пользователей;
- автоматически распределять пожертвования между активными проектами по принципу FIFO.

## Стек
- Python 3.9+
- FastAPI + FastAPI Users
- SQLAlchemy + Alembic (SQLite по умолчанию)

## Подготовка окружения
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
В `.env` должен быть указан `DATABASE_URL=sqlite+aiosqlite:///./fastapi.db` (или ваше подключение).

## Миграции и запуск
```bash
alembic upgrade head
uvicorn app.main:app --reload
```

## Тесты
```bash
pytest
```

API-документация доступна по адресу `/docs` (Swagger) или `/redoc`. Спецификация находится в `openapi.json`.

Автор: Смирнов Вкиктор Евгеньевич