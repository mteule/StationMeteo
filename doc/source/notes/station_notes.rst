station
========

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


