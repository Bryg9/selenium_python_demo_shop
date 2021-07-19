deps:
	pip install -r requirements.txt
	pip install -r test_requirements.txt
test:
	python run.py
lint:
	flake8 pages tests locators.py
