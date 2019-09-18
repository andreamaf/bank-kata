init:
	pip install -r requirements.txt

init-pipenv:
	pipenv install -r requirements.txt

test:
	pytest -v src/tests
