.PHONY: test build clean

test:
	PYTHONPATH=./backend pytest -ra

build:
	@echo "building..."

