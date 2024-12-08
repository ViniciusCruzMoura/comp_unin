# Define the image name as the current directory name
IMAGE_NAME := $(notdir $(PWD))

# Default target (can be used to show help)
.PHONY: help
help:
	@echo "These are common commands used in various situations:"
	@echo ""
	@echo "Usage:"
	@echo "  make COMMAND"
	@echo ""
	@echo "Commands:"
	@echo "  help            Display this help information."
	@echo "  build           Build a new Docker image."
	@echo "  dev             Run the Docker image if it exists; otherwise, build the image and then run it."
	@echo "  compile		 Compile the source code"
	@echo "  run		 	 Run the compiled source code"
	@echo "  rmi             Remove the Docker image by untagging it."
	@echo "  clean           Remove the compiled .class files."
	@echo ""
	@echo "Use 'make build' or 'make dev' for further information on each command."
	@echo ""

# Build the Docker image
.PHONY: build
build:
	docker build --network=host -t $(IMAGE_NAME) .

# Build and run the Docker container
.PHONY: dev
dev:
	@if docker images --format '{{.Repository}}:{{.Tag}}' | grep -q "^$(IMAGE_NAME):latest$$"; then \
		echo "Image $(IMAGE_NAME):latest already exists."; \
	else \
		$(MAKE) build; \
	fi
	docker run -it --rm --network=host --name $(IMAGE_NAME) \
		-v "$(PWD)":/$(IMAGE_NAME) -w /$(IMAGE_NAME) $(IMAGE_NAME) bash

# Remove the Docker image
.PHONY: rmi
rmi:
	docker rmi $(IMAGE_NAME) --force

# Compile the source code
.PHONY: compile
compile:
	docker run -it --rm --network=host --name $(IMAGE_NAME) \
		-v "$(PWD)":/$(IMAGE_NAME) -w /$(IMAGE_NAME) $(IMAGE_NAME) \
		sh -c "javac -encoding UTF-8 -d bin $(wildcard src/**/*.java)"

# Run the class files
.PHONY: run
run:
	docker run -it --rm --network=host --name $(IMAGE_NAME) \
		-v "$(PWD)":/$(IMAGE_NAME) -w /$(IMAGE_NAME) $(IMAGE_NAME) \
		sh -c "cd bin; java $(subst bin/,,$(subst .class,,$(wildcard bin/**/Main.class)))"

# Remove the Docker image
.PHONY: clean
clean:
	docker run -it --rm --network=host --name $(IMAGE_NAME) \
		-v "$(PWD)":/$(IMAGE_NAME) -w /$(IMAGE_NAME) $(IMAGE_NAME) \
		sh -c "rm -rf bin/"

# Default target
.DEFAULT_GOAL := help

