import sys
from .preprocess import Preprocess
from .constants import Functions
from .parse import Parse

preprocessor = Preprocess()
parser = Parse()

def clean(tweet_string):
    cleaned_tweet_string = preprocessor.clean(tweet_string, Functions.CLEAN)
    return cleaned_tweet_string

def tokenize(tweet_string):
    tokenized_tweet_string = preprocessor.clean(tweet_string, Functions.TOKENIZE)
    return tokenized_tweet_string

def parse(tweet_string):
    parsed_tweet_obj = parser.parse(tweet_string)
    return parsed_tweet_obj