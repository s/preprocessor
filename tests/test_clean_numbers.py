import unittest

import preprocessor as p

class PreprocessorTest(unittest.TestCase):
    def test_clean_number_1(self):
        tweet = "1231234"
        p.set_options(p.OPT.NUMBER)
        cleaned_tweeet = p.clean(tweet)
        self.assertEqual(cleaned_tweeet, '')

    def test_clean_number_2(self):
        tweet = "Lorem 198710 ipsum!"
        p.set_options(p.OPT.NUMBER)
        cleaned_tweeet = p.clean(tweet)
        self.assertEqual(cleaned_tweeet, 'Lorem ipsum!')

    def test_clean_number_3(self):
        tweet = "@lorem something 123213 ipsum"
        p.set_options(p.OPT.NUMBER)
        cleaned_tweeet = p.clean(tweet)
        self.assertEqual(cleaned_tweeet, '@lorem something ipsum')

    def test_clean_number_4(self):
        tweet = "123321 21398040 two numbers!"
        p.set_options(p.OPT.NUMBER)
        cleaned_tweeet = p.clean(tweet)
        self.assertEqual(cleaned_tweeet, 'two numbers!')

    def test_clean_number_5(self):
        tweet = "123,000 people"
        p.set_options(p.OPT.NUMBER)
        cleaned_tweeet = p.clean(tweet)
        self.assertEqual(cleaned_tweeet, 'people')

    def test_clean_number_6(self):
        tweet = "#lorem @loremipsum 900,000,000"
        p.set_options(p.OPT.NUMBER)
        cleaned_tweeet = p.clean(tweet)
        self.assertEqual(cleaned_tweeet, '#lorem @loremipsum')

    def test_clean_number_7(self):
        tweet = "World population will be 10,000,000,000 in 2100!"
        p.set_options(p.OPT.NUMBER)
        cleaned_tweeet = p.clean(tweet)
        self.assertEqual(cleaned_tweeet, 'World population will be in !')

    def test_clean_number_8(self):
        tweet = "lorem -987 ipsum"
        p.set_options(p.OPT.NUMBER)
        cleaned_tweeet = p.clean(tweet)
        self.assertEqual(cleaned_tweeet, 'lorem ipsum')

    def test_clean_number_9(self):
        tweet = "lorem -712,917,912,123 ipsum"
        p.set_options(p.OPT.NUMBER)
        cleaned_tweeet = p.clean(tweet)
        self.assertEqual(cleaned_tweeet, 'lorem ipsum')

    def test_clean_number_10(self):
        tweet = "World population will be 10,000,000,000 in 2100!"
        p.set_options(p.OPT.NUMBER)
        cleaned_tweeet = p.clean(tweet)
        self.assertEqual(cleaned_tweeet, 'World population will be in !')