install:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv venv
	uv run pip install -e . jupyterlab nbformat
	
build:
	uv run python scripts/convert.py

docs-deploy:
	uv run mkdocs gh-deploy
