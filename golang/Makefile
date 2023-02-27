.PHONY=help clean test tour

src-directory := src
src-files := $(shell find $(src-directory) -name '*.go')


all: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## clean dev artifacts


.test: $(src-files) $(test-files) Makefile
	go test -cover ./...
	touch .test

test: .test  ## Run tests

tour:
	go install golang.org/x/website/tour@latest
	go run golang.org/x/website/tour@latest
