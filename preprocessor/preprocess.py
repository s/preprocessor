# -*- coding: utf-8 -*-

"""
preprocessor.preprocess
~~~~~~~~~~~~
This module includes preprocess functionality

"""

import re
from .constants import Patterns, Functions
from .utils import Util

class Preprocess:

    tweet = None

    def __init__(self):
        self.repl = None
        self.u = Util()

    def clean(self, tweet_string, repl):

        cleaner_methods = self.u.get_worker_methods(self, 'preprocess_')

        for a_cleaner_method in cleaner_methods:
            token = self.get_token_string_from_method_name(a_cleaner_method)
            method_to_call = getattr(self, a_cleaner_method)

            if repl == Functions.CLEAN:
                tweet_string = method_to_call(tweet_string, '')
            else:
                tweet_string = method_to_call(tweet_string, token)

        tweet_string = self.remove_unneccessary_characters(tweet_string)
        return tweet_string

    def preprocess_urls(self, tweet_string, repl):
        return re.sub(Patterns.URL_PATTERN, repl, tweet_string)

    def preprocess_hashtags(self, tweet_string, repl):
        return re.sub(Patterns.HASHTAG_PATTERN, repl, tweet_string)

    def preprocess_mentions(self, tweet_string, repl):
        return re.sub(Patterns.MENTION_PATTERN, repl, tweet_string)

    def preprocess_reserved_words(self, tweet_string, repl):
        return re.sub(Patterns.RESERVED_WORDS_PATTERN, repl, tweet_string)

    def remove_unneccessary_characters(self, tweet_string):
        return ' '.join(tweet_string.split())

    def get_token_string_from_method_name(self, method_name):
        token_string = method_name.rstrip('s')
        token_string = token_string.split('_')[1]
        token_string = token_string.upper()
        token_string = '$' + token_string + '$'
        return token_string