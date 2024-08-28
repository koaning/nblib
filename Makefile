commit:
	git add . 
	git commit -m "update"
	git push origin main

demo:
	uv run --with cookiecutter cookiecutter -y https://github.com/koaning/nblib