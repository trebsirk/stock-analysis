.PHONY: test build clean

# backend 

test-api:
	PYTHONPATH=./backend pytest -ra

build-api:
	./init.sh

run-api: 
	PYTHONPATH=./backend ./backend/run.sh


run-client:
	cd frontend; npm run serve