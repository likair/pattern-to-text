.PHONY: setup test run build_image run_image export_requirements clean

all: setup test

setup:
	command -v poetry >/dev/null 2>&1 || curl -sSL https://install.python-poetry.org | python3 -
	poetry config virtualenvs.in-project true
	poetry install
	poetry run pre-commit install

test:
	poetry run pytest

run:
	poetry run python src/pattern_to_text.py SST 5 2

build_image:
	docker build -t pattern-to-text .

run_image:
	docker run pattern-to-text SST 5 2

export_requirements:
	poetry export -f requirements.txt --output requirements.txt

clean:
	find . -name "*.pyc" -delete
	rm -rf .venv
	rm -rf .pytest_cache
	rm -f poetry.lock
