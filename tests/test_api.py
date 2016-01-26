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

    def test_parse(self):
        tweet = 'A tweet with #hashtag @mention and http://github.com/s.'
        parsed_tweet = p.parse(tweet)

        self.assertIsNotNone(parsed_tweet.urls)
        self.assertEqual(1, len(parsed_tweet.urls))

        self.assertIsNotNone(parsed_tweet.hashtags)
        self.assertEqual(1, len(parsed_tweet.hashtags))

        self.assertIsNotNone(parsed_tweet.mentions)
        self.assertEqual(1, len(parsed_tweet.mentions))

        self.assertIsNone(parsed_tweet.reserved_words)
        
if __name__ == '__main__':
    unittest.main()
