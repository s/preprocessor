Preprocessor
===================

.. image:: https://travis-ci.org/s/preprocessor.svg?branch=master

Preprocessor is a preprocessing library for tweet data written in Python.

When building Machine Learning systems based on tweet data, a preprocessing is required. This library makes it easy to clean, parse or tokenize the tweets.


Installation
===================
using pip:

.. code-block:: bash

    $ pip install tweet-preprocessor

Usage
===================

Basic cleaning:
^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import preprocessor as p
    >>> p.clean('Preprocessor is #awesome https://github.com/s/preprocessor')
    'Preprocessor is'

Tokenizing:
^^^^^^^^^^^

.. code-block:: python

    >>> p.tokenize('Preprocessor is #awesome https://github.com/s/preprocessor')
    'Preprocessor is $HASHTAG$ $URL$'

Parsing:
^^^^^^^^

.. code-block:: python

    >>> parsed_tweet = p.parse('Preprocessor is #awesome https://github.com/s/preprocessor')
    <preprocessor.parse.ParseResult instance at 0x10f430758>
    >>> parsed_tweet.urls
    [(25:58) => https://github.com/s/preprocessor]
    >>> parsed_tweet.urls[0].start_index
    25
    >>> parsed_tweet.urls[0].match
    'https://github.com/s/preprocessor'
    >>> parsed_tweet.urls[0].end_index
    58
