tests
=====

Tests Sqlalchemy
-----------------

This may be really usefull to change easily the db_url to make test functions:

    >>> import model
    >>> Meter = model.Metering()
    >>> Meter.metadata.bind
    Engine(mysql://monty:passwd@localhost/test_dia)
 
Tests Nose
-----------
First use of python-nose, copying the "Learn Python the Hard Way" methods just to tests the imports.
http://learnpythonthehardway.org/book/ex46.html

The nosetests command should be ran from the /StationMeteo/station_meteo dir, not above.

Then we replace their example bu another using 'unittest'.
http://stephane-klein.info/blog/2013/07/23/python-et-les-tests-nose1-nose2-python-m-unittest/

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
            
the 'nosetests' command still works fully well!!!

Keeping UnitTest now, since it is compatible with nosetests and testing sqlalchemy.

Tests Sqlalchemy Pyramid
--------------------------

    https://www.google.fr/#q=sqlalchemy+Testing

Sqlalchemy in Pyramid uses UniTests:
    http://docs.pylonsproject.org/projects/pyramid/en/1.4-branch/tutorials/wiki2/tests.html

Example with UnitTest:

    http://sontek.net/blog/detail/writing-tests-for-pyramid-and-sqlalchemy

Example with nose:

    http://alextechrants.blogspot.fr/2013/08/unit-testing-sqlalchemy-apps.html

>>> class TestFonctionGet(unittest.TestCase):
...     pass
...     
... 
>>> help(TestFonctionGet.assertRaises())
>>> TestFonctionGet.


unittest.TestCase.assertRaises
------------------------------
From the documentation it seems we need to us it with a 'with' statement and then an 'assertEquals' to test the error code.

>>> import unittest
>>> help(unittest.TestCase.assertRaises)

    http://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
