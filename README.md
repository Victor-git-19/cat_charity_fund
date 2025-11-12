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
git clone https://github.com/Victor-git-19/cat_charity_fund.git
cd cat_charity_fund
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

API-документация: [Swagger UI](/docs) · [ReDoc](/redoc). Спецификация: [openapi.json](openapi.json).

Автор: [Виктор Евгеньевич Смирнов](https://github.com/Victor-git-19)
