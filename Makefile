.PHONY: run ingest db stop reset

run:
	uvicorn app.main:app --reload

ingest:
	python workers/ingest_prices.py

db: 
	docker compose up -d

stop:
	docker compose down

reset:
	docker compose down -v
	docker compose up -d
