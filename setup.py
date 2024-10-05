#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on 2022-Dec-31

@author: oberron
"""
from setuptools import setup, find_packages
from simplepyged import __version__

setup(
    name='simplepyged_ob',
    version=__version__,
    description='A simple Python GEDCOM parser (forked from gburca/simplepyged which forked from dijxtra/simplepyged)',
    long_description=open('README.md', 'r').read(),
    keywords='gedcom, genealogy',
    author='Oberron (based on original work from Nikola Škorić)',
    author_email="one.annum@gmail.com",
    url='https://github.com/oberron/simplepyged',
    license='GPL',
    package_dir={'simplepyged_ob': 'simplepyged'},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Sociology :: Genealogy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False,
    extras_require={
        "dev": [
            "coverage",
            "darglint",
            "flake8",
            "myst_parser",
            "nbsphinx",
            "python-dotenv",
            "Markdown",
            "pyroma",
            "pytest",
            "recommonmark",
            "sphinx",
            "sphinx_markdown_builder",
            "sphinx-rtd-theme",
            "tox",
            "twine",
            "wheel"]}
)
