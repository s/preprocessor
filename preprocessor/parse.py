"""
preprocessor.parse
~~~~~~~~~~~~
This module includes parse functionality

"""

import re
from .utils import *
from .defines import Defines, Patterns

class ParseResult:
    urls = None
    emojis = None
    smileys = None
    numbers = None
    hashtags = None
    mentions = None
    reserved_words = None

    def __init__(self):
        pass


class ParseItem:
    def __init__(self, start_index, end_index, match):
        self.start_index = start_index
        self.end_index = end_index
        self.match = match

    def __repr__(self):
        return '(%d:%d) => %s' % (self.start_index, self.end_index, self.match)


class Parse:

    def __init__(self):
        pass

    def parse(self, tweet_string):
        parse_result_obj = ParseResult()

        parser_methods = get_worker_methods(self, Defines.PARSE_METHODS_PREFIX)

        for a_parser_method in parser_methods:
            method_to_call = getattr(self, a_parser_method)
            attr = a_parser_method.split('_')[1]

            items = method_to_call(tweet_string)
            setattr(parse_result_obj, attr, items)

        return parse_result_obj

    def parser(self, pattern, string):

        match_items = []
        number_match_max_group_count = 2

        for match_object in re.finditer(pattern, string):
            start_index = match_object.start()
            end_index = match_object.end()

            if Patterns.NUMBERS_PATTERN == pattern and number_match_max_group_count == len(match_object.groups()):
                match_str = match_object.groups()[1]
            else:
                match_str = match_object.group()

            parse_item = ParseItem(start_index, end_index, match_str)
            match_items.append(parse_item)

        if len(match_items):
            return match_items

    def parse_urls(self, tweet_string):
        return self.parser(Patterns.URL_PATTERN, tweet_string)

    def parse_hashtags(self, tweet_string):
        return self.parser(Patterns.HASHTAG_PATTERN, tweet_string)

    def parse_mentions(self, tweet_string):
        return self.parser(Patterns.MENTION_PATTERN, tweet_string)

    def parse_reserved_words(self, tweet_string):
        return self.parser(Patterns.RESERVED_WORDS_PATTERN, tweet_string)

    def parse_emojis(self, tweet_string):
        return self.parser(Patterns.EMOJIS_PATTERN, tweet_string)

    def parse_smileys(self, tweet_string):
        return self.parser(Patterns.SMILEYS_PATTERN, tweet_string)

    def parse_numbers(self, tweet_string):
        return self.parser(Patterns.NUMBERS_PATTERN, tweet_string)