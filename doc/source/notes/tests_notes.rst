tests
=====

unittest.TestCase.assertRaises
------------------------------
From the documentation it seems we need to us it with a 'with' statement and then an 'assertEquals' to test the error code.

>>> import unittest
>>> help(unittest.TestCase.assertRaises)
