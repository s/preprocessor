# -*- coding: utf-8 -*-

import os
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

    def test_clean_file(self):
        current_dir = os.getcwd()
        extensions = [p.InputFileType.json, p.InputFileType.text]
        for ext in extensions:
            full_input_path = os.path.join(current_dir, "clean_file_sample" + ext)
            raw_data = p.get_file_contents(full_input_path)
            self.assertIsNotNone(raw_data)

            # Test all option
            check_against = self._get_test_data_for_option(raw_data)
            self._test_clean_file(full_input_path, check_against)

            # Test individual options
            options = [
                p.OPT.URL,
                p.OPT.MENTION,
                p.OPT.HASHTAG,
                p.OPT.RESERVED,
                p.OPT.EMOJI,
                p.OPT.SMILEY,
                p.OPT.NUMBER
            ]
            for opt in options:
                check_against = self._get_test_data_for_option(raw_data, opt)
                self._test_clean_file(full_input_path, check_against, opt)

    def _test_clean_file(self, full_input_path, check_against, *options):
        output_path = p.clean_file(full_input_path, True, options)
        self.assertTrue(os.path.exists(output_path))
        clean_content = p.get_file_contents(output_path)
        p.are_lists_equal(clean_content, check_against)

    def _get_test_data_for_option(self, raw_data, *options):
        clean_data = []
        for d in raw_data:
            clean_data.append(p.clean(d))
        return clean_data

if __name__ == '__main__':
    unittest.main()
