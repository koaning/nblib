from setuptools import setup, find_packages

setup(
    name='{{ cookiecutter.project_slug }}',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.10',
)