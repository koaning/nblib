.PHONY: docs

install:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv venv
	uv run pip install -e . jupyterlab nbformat
	
build:
	uv run --with nbformat scripts/convert.py

docs: build
	uv run --with mkdocs-material --with "mkdocstrings[python]>=0.18" mkdocs serve
