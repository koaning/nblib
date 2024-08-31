.PHONY: docs

install:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv venv
	uv run pip install -e . -r requirements-dev.txt -r requirements.txt jupyterlab nbformat

build:
	rm -rf .tmpdir
	mkdir .tmpdir
	cp -r src/* .tmpdir
	uv pip install -e . -r requirements-dev.txt -r requirements.txt jupyterlab nbformat
	uv run python -m jupyter nbconvert --to notebook --execute .tmpdir/*.ipynb
	uv run --with nbformat scripts/convert.py
	rm -rf .tmpdir

docs: build
	uv run --with mkdocs-material --with "mkdocstrings[python]>=0.18" mkdocs serve
