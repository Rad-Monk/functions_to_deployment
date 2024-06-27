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
	python -m pytest -vv test_*.py

docker:
	docker run -p 127.0.0.1:8082:8080 2840be3385d5

all: install format lint test