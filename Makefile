# Variables
DOCKER_IMAGE_LINTER=alvarofpp/python-linter
ROOT=$(shell pwd)

# Commands
.PHONY: lint
lint:
	@docker pull ${DOCKER_IMAGE_LINTER}
	@docker run --rm -v ${ROOT}:/app ${DOCKER_IMAGE_LINTER} " \
		lint-yaml \
		&& lint-markdown \
		&& lint-python"
