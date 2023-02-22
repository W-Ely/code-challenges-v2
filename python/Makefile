.PHONY=help clean code lint test dev

script-directory := scripts
src-directory := src
test-directory := tests
src-files := $(shell find $(src-directory) -name '*.py' -not \( -path '*__pycache__*' \))
test-files := $(shell find $(test-directory) -name '*.py' -not \( -path '*__pycache__*' \))
script-files := $(shell find $(script-directory) -name '*.sh')
config-files := 

VENV=. .venv/bin/activate

all: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## clean dev artifacts
	rm -rf .venv .lint .test .dev .coverage

.venv/bin/activate:
	python3 -m venv .venv

.dev: requirements.dev.txt requirements.txt .venv/bin/activate
	$(VENV) && pip install -r requirements.txt
	$(VENV) && pip install -r requirements.dev.txt
	touch .dev

dev: .dev ## Setup dev environment

.test: .dev pyproject.toml $(src-files) $(test-files) $(script-files) Makefile
	$(VENV) && coverage run -m unittest && coverage report
	touch .test

test: .test  ## Run tests