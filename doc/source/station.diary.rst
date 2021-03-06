StationMeteo Diary
==================

Date / Clock
-------------
get from the OS a date value that can be easily inserted into the SGBD.
For the moment the easiest solution will be to get the UTC timestamp with:

    >>> import time
    >>> now = time.time()
    >>> now

    1392649039.119693

Solution we found on the first link:
    
import time:

    http://domeu.blogspot.fr/2011/04/time-datetime-manipulation-du-temps-en.html 
    
Other Links:

import datetime:

    http://docs.python.org/2/library/datetime.html

    http://sametmax.com/manipuler-les-dates-et-les-durees-en-python/

        http://sametmax.com/serialiser-et-parser-une-date-en-python-formats-de-strftimestrptime-et-timestamps/

SQLAlchemyError
----------------
May not be precise enough, but we are sure this may catch any exception raised when trying to insert values.
     
    >>> import sqlalchemy
    >>> e = sqlalchemy.exc.ArgumentError
    >>> help(e)
    >>> e = sqlalchemy.exc.SQLAlchemyError
    >>> help(e)
    >>> e = sqlalchemy.exceptions
    >>> help(e)


Sensor_id list
---------------
Code for today: the 'where' clause with a list is somewhere in the doc, so for now we'll retrieve the full list.

    mysql> grant all on test_dia.* to monty@localhost; Flush privileges;

    ~/StationMeteo/station_meteo$ bpython

    >>> import model
    >>> from sqlalchemy import select
    >>> sensor = model.Sensor()
    >>> sens_table = sensor.__table__
    >>> sel = select([sens_table.c.bus_adress, sens_table.c.id])
    >>> print sel
    SELECT `Sensor`.bus_adress, `Sensor`.id 
    FROM `Sensor`
    >>> res = sel.execute()
    >>> res
    <sqlalchemy.engine.base.ResultProxy object at 0x2d288d0>
    >>> dict = {}
    >>> for row in res:
    ...     new_keyval = {row[sens_table.c.bus_adress]: row[sens_table.c.id]}
    ...     dict.update(new_keyval.copy())
    ... 
    >>> dict
    {'CO': 3L, 'TEMP': 1L, 'VOC': 5L, 'Dust': 6L, 'HUM': 2L, 'NO2': 4L}
    >>> type(dict['CO'])
    <type 'long'>
    >>> 

    http://docs.sqlalchemy.org/en/latest/core/tutorial.html#selecting

Not used finally:

    http://stackoverflow.com/questions/5016505/mysql-grant-all-privileges-on-database

    https://stackoverflow.com/questions/19406859/sqlalchemy-convert-select-query-result-to-a-list-of-dicts

Insert metering value
----------------------

    >>> from sqlalchemy import insert
    >>> metering = model.Metering()
    >>> meter_table = metering.__table__
    >>> ins = meter_table.insert()
    >>> ins
    <sqlalchemy.sql.expression.Insert object at 0x2e4ef50>
    >>> print ins
    INSERT INTO `Metering` (date, id, sensor_id, value) VALUES (%s, %s, %s, %s)
    >>> ins.execute()
    /usr/lib/python2.7/dist-packages/sqlalchemy/engine/default.py:331: Warning: Field 'id' doesn't have a default value
      cursor.execute(statement, parameters)
    <sqlalchemy.engine.base.ResultProxy object at 0x2e6c4d0>
    >>> ins = meter_table.insert().values(value='1', date='1', sensor_id='1')
    >>> ins.compile().params
    {u'date': '1', u'sensor_id': '1', u'value': '1'}
    >>> 


    >>> ins = meter_table.insert().values(id= 0, value='1', date='1', sensor_id='1')
    >>> ins.execute()
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
      File "/usr/lib/python2.7/dist-packages/sqlalchemy/sql/expression.py", line 2826, in execute
        return e._execute_clauseelement(self, multiparams, params)
      File "/usr/lib/python2.7/dist-packages/sqlalchemy/engine/base.py", line 2454, in _execute_clauseelement
        return connection._execute_clauseelement(elem, multiparams, params)
      File "/usr/lib/python2.7/dist-packages/sqlalchemy/engine/base.py", line 1584, in _execute_clauseelement
        compiled_sql, distilled_params
      File "/usr/lib/python2.7/dist-packages/sqlalchemy/engine/base.py", line 1698, in _execute_context
        context)
      File "/usr/lib/python2.7/dist-packages/sqlalchemy/engine/base.py", line 1691, in _execute_context
        context)
      File "/usr/lib/python2.7/dist-packages/sqlalchemy/engine/default.py", line 331, in do_execute
        cursor.execute(statement, parameters)
      File "/usr/lib/python2.7/dist-packages/MySQLdb/cursors.py", line 174, in execute
        self.errorhandler(self, exc, value)
      File "/usr/lib/python2.7/dist-packages/MySQLdb/connections.py", line 36, in defaulterrorhandler
        raise errorclass, errorvalue
    IntegrityError: (IntegrityError) (1062, "Duplicate entry '0' for key 'PRIMARY'") 'INSERT INTO `Metering` (date, id, sensor_id, value)     VALUES (%s, %s
    , %s, %s)' ('1', 0, '1', '1')
    >>> ins = meter_table.insert().values(id= 1, value='1', date='1', sensor_id='1')
    >>> ins.execute()
    /usr/lib/python2.7/dist-packages/sqlalchemy/engine/default.py:331: Warning: Data truncated for column 'date' at row 1
      cursor.execute(statement, parameters)
    <sqlalchemy.engine.base.ResultProxy object at 0x2f19810>
    >>> 

NB: When reading model.py ninja-ide detects a problem with the 'id' column line
But the problem doesn't comme from this column but from the "Duplicate entry '0' for key 'PRIMARY'".

In fact by looking for the AUTOINCREMENT mention and sqlalchemy:

    https://www.google.fr/#q=sqlalchemy+id+autoincrement

    http://docs.sqlalchemy.org/en/rel_0_8/dialects/mysql.html#auto-increment-behavior

It appears that when created with sqlalchemy the table will have this functionnality.
But in our tedia2sql generated file this does not appear.

Indeed, dropping the metering table and creating it with sqlalchemy:

    mysql> drop table Metering;

    >>> metering.__table__.create()

    The script DO work pretty well finally.

    mysql> select * from Metering;

Datetime
---------
Some time before we hesitated about which was the best datetime function to choose.
Considering the problem when inserting the metering date, we found more in docsqlalchemy:

    http://docs.sqlalchemy.org/en/rel_0_9/core/types.html#sqlalchemy.types.Date
    
Since the beginning we used "Date" in the Dia diagram, but we have to use a "Datetime" type.
In the doc this datetime corresponds to a datetime.datetime.now() returned value.

Then we will have to change from the Dia diagram and generate another new "model.py"
 
    >>> import time
    >>> print time.time()
    1393299712.16
    >>> import datetime
    >>> print datetime.datetime.now()
    2014-02-25 04:42:22.001683
    >>> clock = datetime.datetime
    >>> print clock.now()
    2014-02-25 07:27:59.671957
    >>> clock.now()
    datetime.datetime(2014, 2, 25, 7, 29, 15, 817655)

since clock.now() seems to render a "constant" object, it may be strongly factorised, appearing only as 

    >>> clock = datetime.datetime

and

    >>> clock.now()

appended in all the "last_meterings" dictionnaries.

TODO: remember to use metering for the ORM, meterings elsewhere.
TODO: Move the db url lines from model to station.py , to use easily the autogenerated model.py file 

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

