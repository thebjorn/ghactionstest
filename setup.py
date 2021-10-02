#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ghactions
"""
# pragma: nocover
import io


import setuptools

version='1.0.0'

setuptools.setup(
    name='ghactionstest',
    version=version,
    packages=['ghactionstest'],
    long_description=io.open('README.rst', encoding='utf8').read(),
    url='https://github.com/thebjorn/ghactionstest',
    license='BSD',
    author='bjorn',
    author_email='bp@datakortet.no',
    description='Test github actions',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
