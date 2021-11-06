all:
	./examples.sh
coverage:
	coverage run -m unittest discover && coverage report -m
docker_build:
	docker image build -t calculus_of_variations .
docker_run:
	docker container run -it -p 8050:8050 calculus_of_variations
pypi_packages:
	pip install --upgrade build twine
pypi_build:
	python -m build
pypi_twine:
	python -m twine upload --repository testpypi dist/*
pypi_clean:
	rm -rf dist src/calculus_of_variations.egg-info
