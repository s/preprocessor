import io
import unittest

import preprocessor as p

class PreprocessorTest(unittest.TestCase):

    def test_clean(self):
        tweet = 'Hello there! @pyistanbul #packathon was awesome. http://packathon.org'
        cleaned_tweeet = p.clean(tweet)
        self.assertEqual(cleaned_tweeet, 'Hello there! was awesome.')

    def test_tokenize(self):
        tweet = 'Packathon was a really #nice challenging. @packathonorg http://packathon.org'
        tokenized_tweet = p.tokenize(tweet)
        self.assertEqual(tokenized_tweet, 'Packathon was a really $HASHTAG$ challenging. $MENTION$ $URL$')

if __name__ == '__main__':
    unittest.main()
