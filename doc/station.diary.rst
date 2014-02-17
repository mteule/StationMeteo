
Date / Clock:
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

SQLAlchemyError:
----------------
May not be precise enough, but we are sure this may catch any exception raised when trying to insert values.
     
    >>> import sqlalchemy
    >>> e = sqlalchemy.exc.ArgumentError
    >>> help(e)
    >>> e = sqlalchemy.exc.SQLAlchemyError
    >>> help(e)
    >>> e = sqlalchemy.exceptions
    >>> help(e)


Sensor_id list:
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

    http://stackoverflow.com/questions/5016505/mysql-grant-all-privileges-on-database

    https://stackoverflow.com/questions/19406859/sqlalchemy-convert-select-query-result-to-a-list-of-dicts


