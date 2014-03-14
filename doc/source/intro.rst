Introduction
============

Context
--------

The :meteo station: will send every 5 minutes a string on the serial port /dev/ttyUSB0.
This strings contains the raw value and the 'readable' value for a set of 6 air quality sensors.

Each of these meterings will have to be stored in a database.

Overview
---------
This raw string has to be parsed into a list of meterings.
The metering of a same string will be inserted one by one in the database.
They will have the same datetime value.
