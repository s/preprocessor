# -*- coding: utf-8 -*-
"""
preprocessor.constants
~~~~~~~~~~~~
This module includes the constant variables used in Preprocessor
"""
import re

PREPROCESS_METHODS_PREFIX = 'preprocess_'
PARSE_METHODS_PREFIX = 'parse_'
PRIORITISED_METHODS = ['urls']

class Patterns:
    URL_PATTERN=re.compile(ur'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')
    HASHTAG_PATTERN = re.compile(r'#\w*')
    MENTION_PATTERN = re.compile(r'@\w*')
    RESERVED_WORDS_PATTERN = re.compile(r'^(RT|FAV)')

    try:
        # UCS-4
        EMOJIS_PATTERN = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
    except re.error:
        # UCS-2
        EMOJIS_PATTERN = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|'
                                    u'([\uD83D][\uDE80-\uDEFF])')

    SMILEYS_PATTERN = re.compile(r"(?::|;|=)(?:-)?(?:\)|\(|D|P|S){1,}")

class Functions:
    CLEAN=1
    TOKENIZE=2
    PARSE=3