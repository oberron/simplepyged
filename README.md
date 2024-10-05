# simplepyged_ob

A simple Python GEDCOM parser

Renamed to simplepyged_ob to avoid naming confusion. Mostly based on simplepyged from dijxtra

v0.1.0 aligns with simplepyged v0.1

## Status of parser


Recognises a subset of GEDCOM 5.5 tags. If you need support for an
unsupported tag, submit an issue (or implement it and send a patch).

## Documentation and Examples

Documentation is in docs/. Examples of how to use this parser are at
docs/examples. If you find documentation and/or examples confusing,
let me know and I'll try to fix it.

## Unit Tests

Unit tests can be executed from the project root directory using:

    PYTHONPATH=simplepyged python -m unittest discover

## Licence

All code is licenced under GPL v.3 or newer.

First commit to dijxtra's repository was based on source from here:
http://ilab.cs.byu.edu/cs460/2006w/assignments/program1.html

Then gburca added python 3 support

This forks added support to pypi

## Forked information

Forked from gburca/simplepyged which forked from dijxtra/simplepyged

## Release on pypi / pypi_test


7.run sphinx-api 
`updates the *.rst in docs/ folder`

> sphinx-apidoc -f -o docs simplepyged

8. run sphinx-build
(updates the read_the_docs folder)

> sphinx-build -b html docs build/html

release on pypi (assumes your pypirc is local to the project)

> python setup.py bdist_wheel
> twine upload -r pypi --config-file=.\.pypirc dist\*