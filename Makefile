.DEFAULT_GOAL := help
ROOT_DIR := ./
VENV_BIN_DIR:=venv/bin

PIP:="$(VENV_BIN_DIR)/pip"

hello:
	@echo "Hello, World!"

help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

define create-venv
python3 -m venv venv
endef

venv: # Create virtual environment
	@$(create-venv)

install: venv # Install project dependencies
	@$(PIP) install -r requirements.txt

freeze: venv # Freeze project dependencies
	@$(PIP) freeze > requirements.txt

migrate: venv # Run database migrations
	@python manage.py migrate

run: venv # Run the development server
	@python manage.py runserver

admin: venv # Create admin superuser
	@python manage.py createsuperuser

shell: venv # Start a Django shell
	@python manage.py shell

test: venv # Run tests with coverage
	@coverage run manage.py test
	@coverage html

check: venv # Perform system check
	@python manage.py check

populatedb: venv # Populate the database with fake records
	@python manage.py populate_db 5

collectstatic: venv # Run the collectstatic command
	@python manage.py collectstatic

clean: ## Clean up the project of unneeded files
	@rm -rf .cache
	@rm -rf htmlcov coverage.xml .coverage
	@find . -name '*.pyc' -delete
	@find . -name 'db.sqlite3' -delete
	@find . -type d -name '__pycache__' -exec rm -r {} \+
	@rm -rf .tox
