# -*- coding: utf-8 -*-
"""
preprocessor.constants
~~~~~~~~~~~~
This module includes the constant variables used in Preprocessor
"""
import re
import sys
from .enum import enum

opts = {
    'URL':'urls',
    'MENTION':'mentions',
    'HASHTAG':'hashtags',
    'RESERVED':'reserved_words',
    'EMOJI':'emojis',
    'SMILEY':'smileys',
    'NUMBER': 'numbers'
}
Options = enum(**opts)
Functions = enum('CLEAN', 'TOKENIZE', 'PARSE')


class Defines:
    PARSE_METHODS_PREFIX = 'parse_'
    FILTERED_METHODS = opts.values()
    PREPROCESS_METHODS_PREFIX = 'preprocess_'
    IS_PYTHON3 = sys.version_info > (3, 0, 0)
    PRIORITISED_METHODS = ['urls', 'mentions', 'hashtags', 'emojis', 'smileys']


class Patterns:
    URL_PATTERN=re.compile(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')
    HASHTAG_PATTERN = re.compile(r'#\w*')
    MENTION_PATTERN = re.compile(r'@\w*')
    RESERVED_WORDS_PATTERN = re.compile(r'^(RT|FAV)')

    try:
        # UCS-4
        EMOJIS_PATTERN = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
    except re.error:
        # UCS-2
        EMOJIS_PATTERN = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')

    SMILEYS_PATTERN = re.compile(r"(?:X|:|;|=)(?:-)?(?:\)|\(|O|D|P|S){1,}", re.IGNORECASE)
    NUMBERS_PATTERN = re.compile(r"(^|\s)(\-?\d+(?:\.\d)*|\d+)")
