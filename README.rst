===================
preprocessor
===================

Preprocessor is a preprocessing library for tweet data written in Python.

When building Machine Learning systems based on tweet data, a preprocessing is required. This library makes it easy to clean, parse or tokenize the tweets.

===================
Installation
===================
using pip::

$ pip install tweet-preprocessor


===================
Usage
===================

.. code-block:: python

    import preprocessor as p
    cleaned_tweet = p.clean("Preprocessor is #awesome https://github.com/s/preprocessor")

    print cleaned_tweet
    #Preprocessor is

    tokenized_tweet = p.tokenize("Preprocessor is #awesome https://github.com/s/preprocessor")

    print tokenized_tweet
    #Preprocessor is $HASHTAG$ $URL$