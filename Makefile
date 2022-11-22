.PHONY: dependencies server live

# DEVELOPMENT
# ~~~~~~~~~~~
# The following rules can be used during development in order to launch development server, generate
# locales, etc.
# --------------------------------------------------------------------------------------------------
dependencies:
	poetry lock; poetry run poe export; poetry run poe export_dev

live:
	poetry run uvicorn app.main:app --workers 4 --host 0.0.0.0 --port 8000

dev:
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# QUALITY ASSURANCE
# ~~~~~~~~~~~~~~~~~
# The following rules can be used to check code quality, import sorting, etc.
# --------------------------------------------------------------------------------------------------

.PHONY: quality fix pylint
quality:
	black --check app
	isort --check app
	flake8 app --count --show-source --statistics

fix:
	black app
	isort app
	flake8 app

pylint:
	pylint app

# Docker shell.
# =============================================================================

.PHONY: shell_on_postgres_container

shell_on_postgres_container:
	docker exec -ti postgres /bin/bash


# Postgres CLI.
# =============================================================================

.PHONY: psql psql_root

# Connect to the `postgres` container as the POSTGRES_USER user.
psql:
	docker exec -ti -e PGPASSWORD=$(POSTGRES_PASSWORD) postgres psql -U $(POSTGRES_USER)
