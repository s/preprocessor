"""
preprocessor.constants
~~~~~~~~~~~~
This module includes the constant variables used in Preprocessor
"""

class Patterns:
    URL_PATTERN=ur'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))'
    HASHTAG_PATTERN = r'#\w*'
    MENTION_PATTERN = r'@\w*'
    RESERVED_WORDS_PATTERN = r'^(RT|FAV)'

class Functions:
    CLEAN=1
    TOKENIZE=2
    PARSE=3