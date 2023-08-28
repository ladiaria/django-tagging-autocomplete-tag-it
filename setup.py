# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
 
long_description = open('README.markdown').read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-tagging-autocomplete',
    version='0.3.1',
    description='Autocompletion for django-tagging',
    long_description=long_description,
    author='Ludwik Trammer',
    author_email='ludwik@gmail.com',
    url='http://code.google.com/p/django-tagging-autocomplete/',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    #zip_safe=False,
    #package_data={},
    #test_suite='tagging_autocomplete.tests.runtests.runtests'
) 
