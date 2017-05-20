Preprocessor
============

.. image:: https://travis-ci.org/s/preprocessor.svg?branch=master

Preprocessor is a preprocessing library for tweet data written in Python.

When building Machine Learning systems based on tweet data, a preprocessing is required. This library makes it easy to clean, parse or tokenize the tweets.

Features
========
Currently supports cleaning, tokenizing and parsing:

- URLs
- Hashtags
- Mentions
- Reserved words (RT, FAV)
- Emojis
- Smileys

Supports Python 2.7 and 3.3+

Usage
=====

Basic cleaning:
^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import preprocessor as p
    >>> p.clean('Preprocessor is #awesome 👍 https://github.com/s/preprocessor')
    'Preprocessor is'

Tokenizing:
^^^^^^^^^^^

.. code-block:: python

    >>> p.tokenize('Preprocessor is #awesome 👍 https://github.com/s/preprocessor')
    'Preprocessor is $HASHTAG$ $EMOJI$ $URL$'

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

Fully customizable:
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> p.set_options(p.OPT.URL, p.OPT.EMOJI)
    >>> p.clean('Preprocessor is #awesome 👍 https://github.com/s/preprocessor')
    'Preprocessor is #awesome'

Preprocessor will go through all of the options by default unless you specify some options.

Available Options:
^^^^^^^^^^^^^^^^^^
==============  ======================
Option Name	  	Option Short Code
==============  ======================
URL		  		:code:`p.OPT.URL`
Mention   		:code:`p.OPT.MENTION`
Hashtag  		:code:`p.OPT.HASHTAG`
Reserved Words  :code:`p.OPT.RESERVED`
Emoji			:code:`p.OPT.EMOJI`
Smiley			:code:`p.OPT.SMILEY`
Number			:code:`p.OPT.NUMBER`
==============  ======================


Installation
===================
using pip:

.. code-block:: bash

    $ pip install tweet-preprocessor

using manual installation:

.. code-block:: bash

    $ python setup.py build
    $ python setup.py install