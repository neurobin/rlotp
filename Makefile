SHELL=/bin/bash

test_deps:
	python -m pip install .[test]

lint:
	ruff src
	mypy --install-types --non-interactive --check-untyped-defs src

test:
	coverage run --branch --include 'src/*' -m unittest discover -s test -v

init_docs:
	cd docs; sphinx-quickstart

docs:
	python -m pip install furo sphinx-copybutton
	sphinx-build docs docs/html

install: clean
	python -m pip install build
	python -m build
	python -m pip install --upgrade $$(echo dist/*.whl)[test]

clean:
	-rm -rf build dist
	-rm -rf *.egg-info

.PHONY: test_deps lint test docs install clean

include common.mk
