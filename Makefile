git:
	git pull
	git add -A
	git commit 
	git push

install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C *.py

test:
	python -m pytest -vv test_hello.py

all: install format lint test