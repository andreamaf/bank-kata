
init:
	python -m pip install -r requirements.txt

test:
	pytest -v src/tests

init-pipenv:
	pipenv install -r requirements.txt

test-pipenv:
	pipenv run pytest -v src/tests
