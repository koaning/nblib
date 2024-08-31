.PHONY: docs

install:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv venv
	uv run pip install -e . -r requirements-dev.txt -r requirements.txt jupyterlab nbformat

build:
	cp -r src/* .tmpdir/.* .
	uv run --with-requirements requirements-dev.txt --with-requirements requirements.txt python -m jupyter nbconvert --to notebook --execute .tmpdir/*.ipynb
	uv run --with nbformat scripts/convert.py

docs: build
	uv run --with mkdocs-material --with "mkdocstrings[python]>=0.18" mkdocs serve
