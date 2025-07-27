# Top‑N Post Recommendations API

Учебный pet‑project на FastAPI + SQLAlchemy: сервис, который отдает топ N постов по количеству лайков. Основан на заданиях финального проекта (часть 1) курса.

## Возможности

- `GET /api/v1/user/{id}` — инфо о пользователе
- `GET /api/v1/post/{id}` — инфо о посте
- `GET /api/v1/user/{id}/feed?limit=10` — действия пользователя 
- `GET /api/v1/post/{id}/feed?limit=10` — действия по посту 
- `GET /api/v1/post/recommendations/?id=123&limit=10` — топ постов по лайкам

Документация Swagger доступна по `/docs`, ReDoc — по `/redoc`.

## Стек

- Python 3.11+
- FastAPI
- SQLAlchemy ORM
- Pydantic
- PostgreSQL

## 🚀 Быстрый старт (локально)

```bash
git clone https://github.com/<your_name>/fastapi-recs.git
cd fastapi-recs
cp .env.example .env  # при необходимости отредактируй
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt  # или poetry install
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

