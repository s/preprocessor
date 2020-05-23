# -*- coding: utf-8 -*-
"""
preprocessor.api
~~~~~~~~~~~~
This module implements the Preprocessor API.

:copyright: (c) 2016 by Said Özcan.
:license: GPLv3, see LICENSE for more details.

"""

from .preprocess import Preprocess
from .defines import Functions, Defines
from .parse import Parse
from .utils import *

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


def clean_file(input_file_path, add_timestamp=False, *options):
    """Cleans given input file in JSON and txt format if it can be found at the given path.
    Returns a stdout for the output file path.
    :param input_file_path: Absolute path for the tweets. Could be either in JSON or .txt format.
    :param add_timestamp: If True, adds current timestamp to the filename
    :return: output file path: str. Returns the file path of the cleaned file.
    :rtype: str
    :raises IOError if the input file empty
    Usage::
      >>> input_file_name = "sample.json"
      >>> p.clean_file(file_name, p.OPT.URL, p.OPT.MENTION)
    """
    file_contents = get_file_contents(input_file_path)
    if not file_contents or len(file_contents) == 0:
        raise IOError("Empty file given at path:" + input_file_path)

    cleaned_content = []
    for line in file_contents:
        cleaned_content.append(clean(line))
    output_path = write_to_output_file(input_file_path, cleaned_content, add_timestamp)
    print("Saved the cleaned tweets to:" + output_path)
    return output_path
