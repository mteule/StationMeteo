import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        self.session = 'foobar'

    def tearDown(self):
        self.session = None

    def test_foo(self):
        a = 1
        self.assertEqual(a, 1)

    def test_bar(self):
        b = 'data' + self.session
        self.assertEqual(b, 'datafoobar')
