Preprocessor
============

![image](https://travis-ci.org/s/preprocessor.svg?branch=master)

Preprocessor is a preprocessing library for tweet data written in Python.

When building Machine Learning systems based on tweet data, a preprocessing is required. This library makes it easy to clean, parse or tokenize the tweets.

Features
========

Currently supports cleaning, tokenizing and parsing:

-   URLs
-   Hashtags
-   Mentions
-   Reserved words (RT, FAV)
-   Emojis
-   Smileys

Supports Python 2.7 and 3.3+

Usage
=====

Basic cleaning:
---------------

```python
>>> import preprocessor as p
>>> p.clean('Preprocessor is #awesome 👍 https://github.com/s/preprocessor')
'Preprocessor is'
```

Tokenizing:
-----------

```python
>>> p.tokenize('Preprocessor is #awesome 👍 https://github.com/s/preprocessor')
'Preprocessor is $HASHTAG$ $EMOJI$ $URL$'
```

Parsing:
--------

```python
>>> parsed_tweet = p.parse('Preprocessor is #awesome https://github.com/s/preprocessor')
<preprocessor.parse.ParseResult instance at 0x10f430758>
>>> parsed_tweet.urls
[(25:58) => https://github.com/s/preprocessor]
>>> parsed_tweet.urls[0].start_index
25
>>> parsed_tweet.urls[0].match
'https://github.com/s/preprocessor'
>>> parsed_tweet.urls[0].end_index
58
```

Fully customizable:
-------------------

```python
>>> p.set_options(p.OPT.URL, p.OPT.EMOJI)
>>> p.clean('Preprocessor is #awesome 👍 https://github.com/s/preprocessor')
'Preprocessor is #awesome'
```

Preprocessor will go through all of the options by default unless you specify some options.

Available Options:
------------------

|Option Name|Option Short Code|
|-----------|-----------------|
|URL|p.OPT.URL|
|Mention|p.OPT.MENTION|
|Hashtag|p.OPT.HASHTAG|
|Reserved Words|p.OPT.RESERVED|
|Emoji|p.OPT.EMOJI|
|Smiley|:code:p.OPT.SMILEY|
|Number|:code:p.OPT.NUMBER|

Available Options:

Installation
============

using pip:

```bash
$ pip install tweet-preprocessor
```

using manual installation:

```bash
$ python setup.py build
$ python setup.py install
```
