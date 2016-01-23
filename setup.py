# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# su anki PyPI yazilimi markdown desteklemiyor
with open('README.rst') as f:
    long_description = f.read()

with open('requirements/requirements.txt') as f:
    install_requires = [line.strip() for line in f.readlines()]

setup(
    name='preprocessor',
    version='0.1',
    description='Elegant tweet preprocessing',
    long_description=long_description,
    author='Said Özcan',
    author_email='saidozcn@gmail.com',
    url='https://github.com/s/preprocessor',
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='ast, codegen, PEP8',
)
