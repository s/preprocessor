import sys
from .preprocessor import Preprocessor

p = Preprocessor()

def clean(tweet_string):
    tweet_string = p.clean(tweet_string, 'CLEAN')
    return tweet_string

def tokenize(tweet_string):
    tweet_string = p.clean(tweet_string, 'TOKENIZE')
    return tweet_string

def parse(tweet_string):
    pass