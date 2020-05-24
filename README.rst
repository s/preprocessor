Preprocessor
============

|image|

Preprocessor is a preprocessing library for tweet data written in
Python. It was written as part of my bachelor thesis in sentiment
analysis. Later I extracted it to a library for broader usage.

When building Machine Learning systems based on tweet data, a
preprocessing is required. This library makes it easy to clean, parse or
tokenize the tweets.

Features
========

Currently supports cleaning, tokenizing and parsing:

-  URLs
-  Hashtags
-  Mentions
-  Reserved words (RT, FAV)
-  Emojis
-  Smileys
-  ``JSON`` and ``.txt`` file support

Preprocessor ``v0.6.0`` supports
``Python 2.7 and 3.5+ on Linux, macOS and Windows``. Tests run on
following setups:

::

    Linux Xenial with Python 2.7, 3.5, 3.6, 3.7
    macOS 10.14 with Python 3.7.5, 3.8.0
    Windows 10.0.17134 with Python 2.7, 3.5.4, 3.6.8

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
    >>> p.clean_file(file_name, options=[p.OPT.URL, p.OPT.MENTION])
    Saved the cleaned tweets to:/tests/artifacts/24052020_013451892752_vkeCMTwBEMmX_clean_file_sample.json

Preprocessing text file:
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    # Text file example
    >>> input_file_name = "sample_txt.txt"
    >>> p.clean_file(file_name, options=[p.OPT.URL, p.OPT.MENTION])
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

using pip:

.. code:: bash

    $ pip install tweet-preprocessor

using manual installation:

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
