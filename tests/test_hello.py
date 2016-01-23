import io
import unittest

import preprocessor


class HelloTest(unittest.TestCase):

    def test_hello(self):
        output = io.StringIO()
        preprocessor.say_hello('cihann', file=output)
        self.assertEqual(output.getvalue(), 'Hello, cihann!\n')


if __name__ == '__main__':
    unittest.main()
