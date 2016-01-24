# -*- coding: utf-8 -*-
import re

class Preprocessor:

    tweet = None

    def __init__(self):

        self.url_pattern=ur'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))'
        self.hashtag_pattern = r'#\w*'
        self.mention_pattern = r'@\w*'
        self.reserved_words = r'^(RT|FAV)'
        self.repl = None

    def clean(self, tweet_string, repl):
        self.repl = repl

        all_methods = dir(self)
        cleaner_methods = filter(lambda x: x.startswith('clean_'), all_methods)

        for a_cleaner_method in cleaner_methods:
            token = self.get_token_string_from_method_name(a_cleaner_method)
            method_to_call = getattr(self, a_cleaner_method)

            if self.repl == 'CLEAN':
                tweet_string = method_to_call(tweet_string, '')
            else:
                tweet_string = method_to_call(tweet_string, token)

        tweet_string = self.remove_unneccessary_characters(tweet_string)
        return tweet_string

    def clean_urls(self, tweet_string, repl):
        return re.sub(self.url_pattern, repl, tweet_string)

    def clean_hashtags(self, tweet_string, repl):
        return re.sub(self.hashtag_pattern, repl, tweet_string)

    def clean_mentions(self, tweet_string, repl):
        return re.sub(self.mention_pattern, repl, tweet_string)

    def clean_reserved_words(self, tweet_string, repl):
        return re.sub(self.reserved_words, repl, tweet_string)

    def remove_unneccessary_characters(self, tweet_string):
        return ' '.join(tweet_string.split())

    def get_token_string_from_method_name(self, method_name):
        token_string = method_name.rstrip('s')
        token_string = token_string.split('_')[1]
        token_string = token_string.upper()
        token_string = '$' + token_string + '$'
        return token_string