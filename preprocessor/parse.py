"""
preprocessor.parse
~~~~~~~~~~~~
This module includes parse functionality

"""

import re
from .utils import Utils
from .defines import Defines, Patterns

class ParseResult:
    urls = None
    emojis = None
    smileys = None
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
        self.u = Utils()

    def parse(self, tweet_string):
        parse_result_obj = ParseResult()

        parser_methods = self.u.get_worker_methods(self, Defines.PARSE_METHODS_PREFIX)

        for a_parser_method in parser_methods:
            method_to_call = getattr(self, a_parser_method)
            attr = a_parser_method.split('_')[1]

            items = method_to_call(tweet_string)
            setattr(parse_result_obj, attr, items)

        return parse_result_obj

    def parser(self, pattern, string):

        items = []

        for match_object in re.finditer(pattern, string):
            if not Defines.IS_PYTHON3:
                parse_item = ParseItem(match_object.start(), match_object.end(), match_object.group().encode('utf-8'))
            else:
                parse_item = ParseItem(match_object.start(), match_object.end(), match_object.group())
            items.append(parse_item)

        if len(items):
            return items

    def parse_urls(self, tweet_string):
        return self.parser(Patterns.URL_PATTERN, tweet_string)

    def parse_hashtags(self, tweet_string):
        return self.parser(Patterns.HASHTAG_PATTERN, tweet_string)

    def parse_mentions(self, tweet_string):
        return self.parser(Patterns.MENTION_PATTERN, tweet_string)

    def parse_reserved_words(self, tweet_string):
        return self.parser(Patterns.RESERVED_WORDS_PATTERN, tweet_string)

    def parse_emojis(self, tweet_string):
        if not Defines.IS_PYTHON3:
            tweet_string = tweet_string.decode('utf-8')
        return self.parser(Patterns.EMOJIS_PATTERN, tweet_string)

    def parse_smileys(self, tweet_string):
        return self.parser(Patterns.SMILEYS_PATTERN, tweet_string)