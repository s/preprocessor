*****
Preprocessor
*****

.. image:: https://travis-ci.org/s/preprocessor.svg?branch=master
    :target: https://travis-ci.org/s/preprocessor

.. image:: https://img.shields.io/pypi/dm/tweet-preprocessor.svg
    :target: https://pypi.python.org/pypi/tweet-preprocessor/

.. image:: https://badge.fury.io/py/tweet-preprocessor.svg
    :target: https://pypi.python.org/pypi/tweet-preprocessor/

.. image:: https://img.shields.io/github/license/s/preprocessor.svg
    :target: https://github.com/s/preprocessor/blob/master/LICENSE.md

.. image:: https://img.shields.io/pypi/pyversions/tweet-preprocessor.svg
    :target: https://pypi.python.org/pypi/tweet-preprocessor/


Preprocessor is a preprocessing library for tweet data written in
Python. When building Machine Learning systems based on tweet and text data, a
preprocessing is required. This is required because of quality of the data as well as dimensionality reduction purposes. 

This library makes it easy to clean, parse or tokenize the tweets so you don't have to write the same helper functions over and over again ever time.

Features
========

Currently supports cleaning, tokenizing and parsing:

-  URLs
-  Hashtags
-  Mentions
-  Reserved words (RT, FAV)
-  Emojis
-  Smileys
-  Numbers
-  ``JSON`` and ``.txt`` file support

Preprocessor ``v0.6.0`` supports
``Python 3.4+ on Linux, macOS and Windows``. Tests run on
following setups:

::

    Linux Xenial with Python 3.4.8, 3.5.6, 3.6.7, 3.7.1, 3.8.0, 3.8.3+
    macOS with Python 3.7.5, 3.8.0
    Windows with Python 3.5.4, 3.6.8

Usage
=====

Basic cleaning:
---------------

.. code:: python

    >>> import preprocessor as p
    >>> p.clean('Preprocessor is #awesome 👍 https://github.com/s/preprocessor')
    'Preprocessor is'

Tokenizing:
-----------

.. code:: python

    >>> p.tokenize('Preprocessor is #awesome 👍 https://github.com/s/preprocessor')
    'Preprocessor is $HASHTAG$ $EMOJI$ $URL$'

Parsing:
--------

.. code:: python

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
-------------------

.. code:: python

    >>> p.set_options(p.OPT.URL, p.OPT.EMOJI)
    >>> p.clean('Preprocessor is #awesome 👍 https://github.com/s/preprocessor')
    'Preprocessor is #awesome'

Preprocessor will go through all of the options by default unless you
specify some options.

Processing files:
-----------------

Preprocessor currently supports processing ``.json`` and ``.txt``
formats. Please see below examples for the correct input format.

Example JSON file
~~~~~~~~~~~~~~~~~

.. code:: json

    [
        "Preprocessor now supports files. https://github.com/s/preprocessor",
        "#preprocessing is a cruical part of @ML projects.",
        "@RT @Twitter raw text data usually has lots of #residue. http://t.co/g00gl"
    ]

Example Text file
~~~~~~~~~~~~~~~~~

::

    Preprocessor now supports files. https://github.com/s/preprocessor
    #preprocessing is a cruical part of @ML projects.
    @RT @Twitter raw text data usually has lots of #residue. http://t.co/g00gl

Preprocessing JSON file:
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    # JSON example
    >>> input_file_name = "sample_json.json"
    >>> p.clean_file(input_file_name, options=[p.OPT.URL, p.OPT.MENTION])
    Saved the cleaned tweets to:/tests/artifacts/24052020_013451892752_vkeCMTwBEMmX_clean_file_sample.json

Preprocessing text file:
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    # Text file example
    >>> input_file_name = "sample_txt.txt"
    >>> p.clean_file(input_file_name, options=[p.OPT.URL, p.OPT.MENTION])
    Saved the cleaned tweets to:/tests/artifacts/24052020_013451908865_TE9DWX1BjFws_clean_file_sample.txt

Available Options:
~~~~~~~~~~~~~~~~~~

+------------------+---------------------+
| Option Name      | Option Short Code   |
+==================+=====================+
| URL              | p.OPT.URL           |
+------------------+---------------------+
| Mention          | p.OPT.MENTION       |
+------------------+---------------------+
| Hashtag          | p.OPT.HASHTAG       |
+------------------+---------------------+
| Reserved Words   | p.OPT.RESERVED      |
+------------------+---------------------+
| Emoji            | p.OPT.EMOJI         |
+------------------+---------------------+
| Smiley           | p.OPT.SMILEY        |
+------------------+---------------------+
| Number           | p.OPT.NUMBER        |
+------------------+---------------------+

Installation
============

Using pip:

.. code:: bash

    $ pip install tweet-preprocessor


Using Anaconda:

.. code:: bash
    
    $ conda install -c saidozcan tweet-preprocessor

Using manual installation:

.. code:: bash

    $ python setup.py build
    $ python setup.py install

Contributing
============

Are you willing to contribute to preprocessor? That's great! Please
follow below steps to contribute to this project:

#. Create a bug report or a feature idea using the templates on Issues
   page.

#. Fork the repository and make your changes.

#. Open a PR and make sure your PR has tests and all the checks pass.

#. And that's all!

.. |image| image:: https://travis-ci.org/s/preprocessor.svg?branch=master
