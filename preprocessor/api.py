# -*- coding: utf-8 -*-
"""
preprocessor.api
~~~~~~~~~~~~
This module implements the Preprocessor API.

:copyright: (c) 2016 by Said Özcan.
:license: GPLv3, see LICENSE for more details.

"""

import sys
from .preprocess import Preprocess
from .defines import Functions, Defines
from .parse import Parse

preprocessor = Preprocess()
parser = Parse()

def clean(tweet_string):
    """Cleans irrelevant information from a tweet text`.
    :param tweet_string: A tweet text to clean.
    :return: Cleaned tweet text.
    :rtype: string
    Usage::
      >>> import preprocessor
      >>> cleaned_tweet = preprocessor.clean("Preprocessor is #awesome https://github.com/s/preprocessor")
        Preprocessor is
    """
    cleaned_tweet_string = preprocessor.clean(tweet_string, Functions.CLEAN)
    return cleaned_tweet_string

def tokenize(tweet_string):
    """Tokenizes irrelevant information in a tweet text`.
    :param tweet_string: A tweet text to tokenize.
    :return: Tokenized tweet text.
    :rtype: string
    Usage::
      >>> import preprocessor
      >>> tokenized_tweet = preprocessor.tokenize("Preprocessor is #awesome https://github.com/s/preprocessor")
        Preprocessor is $HASHTAG$ $URL$
    """
    tokenized_tweet_string = preprocessor.clean(tweet_string, Functions.TOKENIZE)
    return tokenized_tweet_string

def parse(tweet_string):
    """Parses given a tweet text and returns an object`.
    :param tweet_string: A tweet text to parse.
    :return: Parsed tweet.
    :rtype: preprocessor.parse.ParseResult
    Usage::
      >>> import preprocessor
      >>> parsed_tweet = preprocessor.parse("Preprocessor is #awesome https://github.com/s/preprocessor")
        preprocessor.parse.ParseResult
      >>> parsed_tweet.urls
        [(25:58) => https://github.com/s/preprocessor]
      >>> parsed_tweet.urls[0].start_index
        25
    """
    parsed_tweet_obj = parser.parse(tweet_string)
    return parsed_tweet_obj

def set_options(*args):
    """Sets desired options for preprocessing`.
    :param *args: A number of preprocessor.OPT options
    :return: void
    :rtype: void
    Usage::
      >>> import preprocessor
      >>> preprocessor.set_options(preprocessor.OPT.URL, preprocessor.OPT.SMILEY)
    """
    Defines.FILTERED_METHODS = list(args)