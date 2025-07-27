run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --app-dir src

test:
	pytest -q

lint:
	flake8 src

fmt:
	black src && isort src

docker-up:
	docker-compose up --build

docker-down:
	docker-compose down

