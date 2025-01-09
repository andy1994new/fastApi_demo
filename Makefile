install:
	pip3 install --upgrade pip && pip3 install -r requirements.txt
format:
	black *.py mylib/*.py
lint:
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
deploy:
	#deploy

all: install lint test