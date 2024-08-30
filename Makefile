commit:
	git add . 
	git commit -m "update"
	git push origin main

demo: commit
	rm -rf proj
	uv run --with cookiecutter cookiecutter https://github.com/koaning/nblib
	cd proj
	make docs
