#!/usr/bin/env python
# -*- coding: utf8 -*-
from setuptools import setup, find_packages

requirements = [
    'Flask>=0.8',
    'unqlite>=0.5'
]

setup(
    name='Flask-UnQLite',
    version='0.5.1',
    license='MIT',
    url='https://github.com/snakeego/flask-unqlite',
    author='Snake',
    author_email='snakeego86@ya.ru',
    description='Add Key-Value storage for Flask application based on UnQLite DB',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Framework :: Flask',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=requirements,
)
