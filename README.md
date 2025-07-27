# Top‑N Post Recommendations API

Учебный pet‑project на **FastAPI + SQLAlchemy**: сервис, который отдаёт топ *N* постов по количеству лайков. Основан на 1‑й части финального проекта курса.

---

## Возможности (REST API)

| Метод | URL                                   | Описание                               | Параметры |
|-------|----------------------------------------|-----------------------------------------|-----------|
| GET   | `/api/v1/user/{id}`                    | Инфо о пользователе                     | —         |
| GET   | `/api/v1/post/{id}`                    | Инфо о посте                            | —         |
| GET   | `/api/v1/user/{id}/feed?limit=10`      | Действия пользователя                   | `limit`   |
| GET   | `/api/v1/post/{id}/feed?limit=10`      | Действия по посту                       | `limit`   |
| GET   | `/api/v1/post/recommendations/?id=123&limit=10` | Топ постов по лайкам            | `id`, `limit` |

Документация: 
- Swagger UI — `/docs` 
- ReDoc — `/redoc`

---

## 🧱 Стек

- Python 3.11+
- FastAPI
- SQLAlchemy ORM
- Pydantic
- PostgreSQL

(опционально: Docker, pytest и т.д.)

---

## Быстрый старт (локально)

```bash
git clone https://github.com/bbs-caleb/fastapi-recs.git
cd fastapi-recs

cp .env.example .env         
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Запуск
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --app-dir src

