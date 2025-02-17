# Django Boilerplate for fast setup

This is a Django-based application that uses PostgreSQL, python-decouple for environment management, and pre-commit hooks for code quality checks. Below is a step-by-step guide for setting up the project on a local machine.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Clone the Repository](#clone-the-repository)
3. [Environment Variables](#environment-variables)
4. [Local Setup (Using Makefile)](#local-setup-using-makefile)
5. [Running the App](#running-the-app)
6. [Pre-commit Hooks](#pre-commit-hooks)
7. [Useful Make Targets](#useful-make-targets)
8. [Docker (Optional)](#docker-optional)
9. [License](#license)

---

## Prerequisites

1. **Python 3.12** (or a similar Python 3.x environment)
2. **pip** (comes installed with Python 3.x)
3. **PostgreSQL** (if you want to use a local Postgres DB)
4. **Make** (if you're on Windows, install [Make for Windows](http://gnuwin32.sourceforge.net/packages/make.htm) or use WSL)

- Python 3.8 or higher
- PostgreSQL installed and running
- **Database Setup (Important!):**
  - Either:
    1. Create a PostgreSQL database with these default credentials:
       ```
       Database name: your_db_name
       Username: your_username
       Password: your_password
       Host: localhost
       Port: 5432
       ```
    2. OR modify the database credentials in `.env` to match your existing database before running `make setup`

*(If you don't have PostgreSQL locally, you can still test with SQLite by adjusting your Django `settings.py`, but Postgres is recommended.)*

---

## Clone the Repository

```bash
git clone https://github.com/13aksh/django_boilerplate.git <YOUR_APP_NAME>
cd <YOUR_APP_NAME>
```

---

## Environment Variables

1. **Create a `.env` file** at the project root (same level as `manage.py`).
2. Add your required variables. For example:

   ```bash
   DJANGO_SECRET_KEY="some_local_dev_secret"
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

   Database name: your_db_name
   Username: your_username
   Password: your_password
   Host: localhost
   Port: 5432
   ```

3. **Do not** commit `.env` to source control. Make sure `.env` is in your `.gitignore`.

---

## Local Setup (Using Makefile)

This project comes with a `Makefile` that simplifies the setup process. It will:

1. Check for the `.env` file and required environment variables.
2. Create a Python virtual environment.
3. Install required packages from `requirements.txt`.
4. Run migrations on the database.
5. Prompt you to create a Django superuser.
6. Install **pre-commit** hooks.

To do all of the above in one command:

```bash
make setup
```

> **Tip**: If you need to customize anything (e.g., DB credentials), edit your `.env` before running this command.

---

## Running the App

After a successful setup:

1. **Activate** your virtual environment (if it isn't already):
   ```bash
   source venv/bin/activate
   ```
2. **Run** the Django development server:
   ```bash
   python manage.py runserver
   ```
3. Visit `http://127.0.0.1:8000/` to see the application.

---

## Pre-commit Hooks

We use [pre-commit](https://pre-commit.com/) to run various checks (e.g., **Black** for code formatting, trailing whitespace fixer, etc.) automatically before you commit code.

- **Installation** is handled by `make setup`.
- Each time you commit, the hooks will run.
- If you want to run them manually:
  ```bash
  pre-commit run --all-files
  ```

---

## Useful Make Targets

- `make setup`: Runs the complete setup (env check, install, migrate, createsuperuser, pre-commit install).
- `make check-env`: Checks for `.env` presence and required variables.
- `make venv`: Creates a Python virtual environment called `venv/`.
- `make install-reqs`: Installs packages from `requirements.txt`.
- `make migrate`: Runs Django migrations.
- `make create-superuser`: Prompts you to create a Django admin user.
- `make enable-pre-commit`: Installs pre-commit hooks.

> For a full list of targets, run `make help`.

---

## Docker (Optional)

If you prefer a **Docker-based** workflow or want to deploy with containers:

1. **Build** the image:
   ```bash
   docker build -t <YOUR_APP_NAME>:latest .
   ```
2. **Run** the container:
   ```bash
   docker run -p 8000:8000 <YOUR_APP_NAME>:latest
   ```
3. [Work in progress] **Docker Compose**: You can create a `docker-compose.yml` if you want to orchestrate **Django + Postgres** together. See the sample in the project (if provided) or create your own.