
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



