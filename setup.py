#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'dash>=0.21.1',
    'dash-renderer>=0.13.0',
    'dash-html-components>=0.11.0',
    'dash-core-components>=0.23.0',
    'plotly>=2.7.0'
    # TODO: put package requirements here
]

setup_requirements = [
    'bumpversion>=0.5.3',
    'wheel>=0.29.0',
    'watchdog>=0.8.3',
    'Sphinx>=1.4.8',
    'gunicorn>=19.9.0'
    # TODO(moodule): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest>=2.9.2',
    'pytest-runner>=2.11.1',
    'flake8>=2.6.0',
    'tox>=2.3.1',
    'coverage>=4.1'
    # TODO: put package test requirements here
]

setup(
    name='driven',
    version='0.0.0',
    description="Have your machiness designed automatically according to your objectives.",
    long_description=readme + '\n\n' + history,
    author="David Mougeolle",
    author_email='david.mougeolle@moodule.net',
    url='https://github.com/moodule/driven-moodule',
    packages=find_packages(include=['driven']),
    entry_points={
        'console_scripts': [
            'driven=driven.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='driven',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
