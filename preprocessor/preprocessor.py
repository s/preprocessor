# -*- coding: utf-8 -*-
import re

class Preprocessor:

    def __init__(self):
        self.patterns = {
            'url':ur'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))',
            'hashtag':r'#\w*',
            'mention':r'@\w*',
            'reserved_words':r'^(RT|FAV)*'
        }

    def find_all(self, tweet_string):
        matches = {}
        for type, pattern in self.patterns.iteritems():
            if type != 'emojis':
                matches[type] = self.find(tweet_string, pattern)
            else:
                pass
        print matches

    def find(self, string, pattern):
        matches = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer(pattern, string)]
        return matches