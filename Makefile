install:
	pip3 install --upgrade pip && pip3 install -r requirements.txt
format:
	black *.py mylib/*.py
lint:
	pylint --disable=R,C *.py mylib/*.py
test:
	python3 -m pytest -vv test_*.py
build:
	#build
	docker build -t fastapi_demo .
run:
	docker run -d -p 8000:8000 fastapi_demo
deploy:
	#deploy
	aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 135808921973.dkr.ecr.eu-west-1.amazonaws.com
	docker build -t fastapi .
	docker tag fastapi:latest 135808921973.dkr.ecr.eu-west-1.amazonaws.com/fastapi:latest
	docker push 135808921973.dkr.ecr.eu-west-1.amazonaws.com/fastapi:latest

all: install lint test