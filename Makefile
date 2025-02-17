SHELL := /bin/bash
.DEFAULT_GOAL := help

ENV_FILE := .env

.PHONY: help check-env venv install-reqs migrate create-superuser enable-pre-commit setup

help:
	@echo "Usage: make [target]"
	@echo "Available targets:"
	@echo "  check-env"
	@echo "  venv"
	@echo "  install-reqs"
	@echo "  migrate"
	@echo "  create-superuser"
	@echo "  enable-pre-commit"
	@echo "  setup"

check-env:
	@test -f $(ENV_FILE) || (echo "[ERROR] .env file not found. Please create one." && exit 1)
	@. $(ENV_FILE); \
	if [ -z "$$DJANGO_SECRET_KEY" ]; then \
		echo "[ERROR] DJANGO_SECRET_KEY not set in .env"; \
		exit 1; \
	fi
	@echo "[OK] All required env vars appear to be set."

venv:
	python -m venv venv

install-reqs:
	. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

migrate:
	. venv/bin/activate && python manage.py migrate

create-superuser:
	@read -p "Enter superuser email: " email; \
	. venv/bin/activate && python manage.py createsuperuser --email $$email --username $$email

enable-pre-commit:
	. venv/bin/activate && pre-commit install

setup: check-env venv install-reqs migrate create-superuser enable-pre-commit
	@echo "[INFO] Setup complete."
