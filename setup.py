# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# su anki PyPI yazilimi markdown desteklemiyor
with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tweet-preprocessor',
    version='0.5.0',
    description='Elegant tweet preprocessing',
    long_description=long_description,
    author='Said Özcan',
    author_email='saidozcn@gmail.com',
    url='https://github.com/s/preprocessor',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='machine learning, preprocessing, tweet',
)
