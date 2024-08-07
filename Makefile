#Makefile

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	# python3 -m pip install --user dist/*.whl
	python3 -m pip install dist/*.whl

package-uninstall:
	python3 -m pip uninstall dist/*.whl

brain-games:
	poetry run brain-games

lint:
	poetry run flake8 brain_games

venv:
	source ../test_venv/bin/activate

venv-new:
	python3 -m venv ../test_venv
