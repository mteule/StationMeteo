tests
=====

unittest.TestCase.assertRaises
------------------------------
From the documentation it seems we need to us it with a 'with' statement and then an 'assertEquals' to test the error code.

>>> import unittest
>>> help(unittest.TestCase.assertRaises)

    http://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
