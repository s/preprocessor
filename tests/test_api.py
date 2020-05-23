# -*- coding: utf-8 -*-

import os
import unittest
import preprocessor as p


class PreprocessorTest(unittest.TestCase):
    _artifacts_dir_name = "artifacts"

    def test_clean(self):
        tweet = "Hello there! @pyistanbul #packathon was awesome exp 😀. http://packathon.org"
        p.set_options(p.OPT.URL, p.OPT.HASHTAG, p.OPT.MENTION, p.OPT.EMOJI, p.OPT.SMILEY)
        cleaned_tweet = p.clean(tweet)
        self.assertEqual(cleaned_tweet, 'Hello there! was awesome exp .')

    def test_clean_urls(self):
        tweet = 'canbe foundathttp://www.osp.gatech.edu/rates/(http://www.osp.gatech.edu/rates/).'
        p.set_options(p.OPT.URL)
        cleaned_tweet = p.clean(tweet)
        self.assertEqual("canbe foundat.", cleaned_tweet)

        tweet = 'Nature：先日フランスで起きた臨床試験事故https://t.co/aHk5ok9CDg 原因究明まだなので早急な印象がするけど、低用量投与を1回' \
                'やった後で、(別のボランティアに）高用量の投与とかしてる試験方式にも問題があるだろうみたいなことを書いてる'
        cleaned_tweet = p.clean(tweet)
        self.assertEqual('Nature：先日フランスで起きた臨床試験事故 原因究明まだなので早急な印象がするけど、'
                         '低用量投与を1回やった後で、(別のボランティアに）高用量の投与とかしてる試験方式にも問題があるだろうみたいなことを書いてる',
                         cleaned_tweet)

        tweet = '[https://link.springer.com/article/10.1007/s10940\\-016\\-9314\\-9]'
        cleaned_tweet = p.clean(tweet)
        self.assertEqual('[]', cleaned_tweet)

        tweet = '(https://link.springer.com/article/10.1007/s10940-016-9314-9)'
        cleaned_tweet = p.clean(tweet)
        self.assertEqual('()', cleaned_tweet)

        tweet = 'check this link: https://fa.wikipedia.org/wiki/%D8%AD%D9%85%D9%84%D9%87_%D8%A8%D9%87_%DA%A9%D9%88%DB%8C' \
                '_%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87_%D8%AA%D9%87%D8%B1%D8%A7%D9%86_(%DB%B1%DB%B8%E2%80%93%DB%B2%' \
                'DB%B3_%D8%AA%DB%8C%D8%B1_%DB%B1%DB%B3%DB%B7%DB%B8) …'
        cleaned_tweet = p.clean(tweet)
        self.assertEqual('check this link: …', cleaned_tweet)

    def test_clean_smileys(self):
        tweet = "😀 :) expression experience zoxo xoyo 💁‍♂️🙍‍♀️🙍‍♀️🧢🐄🧑‍🤝‍🧑"
        p.set_options(p.OPT.SMILEY, p.OPT.EMOJI)
        cleaned_tweet = p.clean(tweet)
        self.assertEqual('expression experience zoxo xoyo', cleaned_tweet)

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
        current_dir = os.path.dirname(__file__)
        artifacts_dir = os.path.join(current_dir, self._artifacts_dir_name)
        extensions = [p.InputFileType.json, p.InputFileType.text]
        for ext in extensions:
            full_input_path = os.path.join(artifacts_dir, "clean_file_sample" + ext)
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

    def test_escape_chars(self):
        p.set_options(p.OPT.ESCAPE_CHAR)
        input_str = u"\x01\x02\x03\x04I \x05\x06\x07\x10\x11have \x12\x13\x14" \
                    "\x15\x16\x17\x20escaped!\a\b\n\r\t\b\f"
        cleaned_str = p.clean(input_str)
        self.assertEqual("I have escaped!", cleaned_str)

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
