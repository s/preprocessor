# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8', errors='ignore') as f:
    long_description = f.read()


setup(
    name='tweet-preprocessor',
    version='0.6.0',
    description='Elegant tweet preprocessing',
    long_description=long_description,
    author='Said Özcan',
    author_email='',
    url='https://github.com/s/preprocessor',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='machine learning, preprocessing, processing, tweet, tokenizing, dimensionality reduction',
)
