.PHONY=help clean code lint test dev

all: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## clean dev artifacts

dev:  ## Setup dev environment
	cd python && $(MAKE) dev

test:  ## Run tests
	cd python && $(MAKE) test
	cd golang && $(MAKE) test
