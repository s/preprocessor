===================
Preprocessor
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

####Basic cleaning:

    >>> import preprocessor as p
    >>> cleaned_tweet = p.clean("Preprocessor is #awesome https://github.com/s/preprocessor")
          # Preprocessor is

####Tokenizing:

    >>> tokenized_tweet = p.tokenize("Preprocessor is #awesome https://github.com/s/preprocessor")
	      # Preprocessor is $HASHTAG$ $URL$

####Parsing:

    >>> parsed_tweet = p.parse("Preprocessor is #awesome https://github.com/s/preprocessor")
          # <preprocessor.parse.ParseResult instance at >
    >>> parsed_tweet.urls
          # [(25:58) => https://github.com/s/preprocessor]
    >>> parsed_tweet.urls[0].start_index
          # 25