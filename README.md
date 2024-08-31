# nblib

> A simple way to write a python package from a Jupyter notebook

## What?

The idea is pretty simple. Run this: 

```python
uv run --with cookiecutter cookiecutter https://github.com/koaning/nblib
```

And this will start a new project that can be written completely from a Jupyter notebook. From the newly created folder you can run everything by running:

1. `make install` to install the project
2. `make build` to export the notebooks to a python package
3. `make docs` to show the docs
4. `make pypi` to upload the package to pypi

The assumption is that all testing takes place in the notebook.

## Details?

The big idea here is that if the intended usage of a tool is a Jupyter notebook then it might also make sense to develop in it. This is especially true if one is developing Jupyter widgets, but some numeric code may also benefit from it. 

Please have a look at the `__init__.ipynb` file to see how this works. It uses a commenting system to keep track of what should be exported to the docs and what should go into the package. The `## DOCSONLY` command is used to mark cells that should only be exported to the docs and not the Python package. The `## SHOW` command is used to mark cells that should be shown in the docs.

One the desciptive side is generated this tool will also generate API docs by leveraging the `mkdocstrings` package.

## When?

The use-case is that sometimes you only need to write a simple technique that can be fully implemented in a single notebook. For those use-cases, this approach is pretty neat. This approach is *heavily* inspired by [Jeremy Howards nbdev](https://github.com/jupyter/nbdev) project but prefers slightly different tools and a different workflow. This project puts a focus on `mkdocs-material` for documentation and `uv` for many development tasks.

This work really should not be used by everyone and it is mainly meant for something for myself personally.

