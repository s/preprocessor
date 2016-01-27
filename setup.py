# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# su anki PyPI yazilimi markdown desteklemiyor
with open('README.rst') as f:
    long_description = f.read()

setup(
    name='tweet-preprocessor',
    version='0.3.0',
    description='Elegant tweet preprocessing',
    long_description=long_description,
    author='Said Özcan',
    author_email='saidozcn@gmail.com',
    url='https://github.com/s/preprocessor',
    packages=find_packages(),
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
    keywords='machine learning, preprocessing, tweet',
)
