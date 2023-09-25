.PHONY: test build clean

test:
	PYTHONPATH=./backend pytest -ra

build:
	@echo "building..."

run-backend: 
	./backend/run.sh