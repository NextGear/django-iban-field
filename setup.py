#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    url                  = 'https://github.com/Chedi/django-iban-field',
    name                 = 'django-iban-field',
    author               = 'Chedi Toueiti',
    license              = 'GNU General Public License v3 (GPLv3)',
    version              = '0.1',
    packages             = find_packages(),
    keywords             = 'django iban field',
    platforms            = ['any'],
    description          = 'IBAN field for django with validation and optional postgresql in database constraint checking',
    author_email         = 'chedi.toueiti@gmail.com',
    long_description     = open('README.rst').read(),
    include_package_data = True,

    classifiers=[
        'Framework :: Django :: 1.8',
        'Environment :: Web Environment',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
