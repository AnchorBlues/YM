# -*- coding: utf-8 -*-

# Learn more: https://github.com/AnchorBlues/ym/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ym',
    version='0.1.3',
    description='YearMonth object for Python',
    long_description=readme,
    author='Yu Umegaki',
    author_email='yu.umegaki@gmail.com',
    install_requires=['pandas'],
    url='https://github.com/AnchorBlues/ym',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')), 
    test_suite='tests'
)
