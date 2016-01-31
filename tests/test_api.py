# -*- coding: utf-8 -*-

import io
import unittest

import preprocessor as p

class PreprocessorTest(unittest.TestCase):

    def test_clean(self):
        tweet = "Hello there! @pyistanbul #packathon was awesome 😀. http://packathon.org"
        p.set_options(p.OPT.URL, p.OPT.HASHTAG, p.OPT.MENTION, p.OPT.EMOJI, p.OPT.SMILEY)
        cleaned_tweeet = p.clean(tweet)
        self.assertEqual(cleaned_tweeet, 'Hello there! was awesome .')

    def test_tokenize(self):
        tweet = 'Packathon was a really #nice :) challenging 👌. @packathonorg http://packathon.org'
        p.set_options(p.OPT.URL, p.OPT.HASHTAG, p.OPT.MENTION, p.OPT.EMOJI, p.OPT.SMILEY)
        tokenized_tweet = p.tokenize(tweet)
        self.assertEqual(tokenized_tweet, 'Packathon was a really $HASHTAG$ $SMILEY$ challenging $EMOJI$. $MENTION$ $URL$')

    def test_parse(self):
        tweet = 'A tweet with #hashtag :) @mention 😀 and http://github.com/s.'
        p.set_options(p.OPT.URL, p.OPT.HASHTAG, p.OPT.MENTION, p.OPT.EMOJI, p.OPT.SMILEY)
        parsed_tweet = p.parse(tweet)

        self.assertIsNotNone(parsed_tweet.urls)
        self.assertEqual(1, len(parsed_tweet.urls))

        self.assertIsNotNone(parsed_tweet.hashtags)
        self.assertEqual(1, len(parsed_tweet.hashtags))

        self.assertIsNotNone(parsed_tweet.mentions)
        self.assertEqual(1, len(parsed_tweet.mentions))

        self.assertIsNone(parsed_tweet.reserved_words)

        self.assertIsNotNone(parsed_tweet.emojis)
        self.assertEqual(1, len(parsed_tweet.emojis))
        self.assertEqual("😀", parsed_tweet.emojis[0].match)

        self.assertIsNotNone(parsed_tweet.smileys)
        self.assertEqual(1, len(parsed_tweet.smileys))
        self.assertEqual(":)", parsed_tweet.smileys[0].match)

    def test_set_options(self):
        tweet = 'Preprocessor now has custom #options support! https://github.com/s/preprocessor'
        p.set_options(p.OPT.URL)
        parsed_tweet = p.parse(tweet)

        self.assertIsNone(parsed_tweet.hashtags)
        self.assertIsNotNone(parsed_tweet.urls)
        
if __name__ == '__main__':
    unittest.main()
