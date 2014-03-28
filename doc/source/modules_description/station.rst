
station_meteo.station
---------------------

Documentation
^^^^^^^^^^^^^

.. automodule:: station_meteo.station
   :members:

Example of use
^^^^^^^^^^^^^^^

Running the loop() with a continous input of raw string csv data:

>>> import station
>>> stat = station.Station()
>>> def return_good_data():
...     raw_string = (
...             "TEMP,-1,17.40,HUM,-1,57.50,NO2,4236,15.4445400238,CO,125283," +
...             "17411.0546875000,VOC,141338,22.7283306121,Dust,2776,0.0003270847" +
...             "\n\r")
...     return raw_string
...     
... 
>>> stat.ser.readline = return_good_data
>>> stat.loop()

Then checking the resulted added values in the dbms. 
Depending of the computers, we note that the quantity of raw strings treated every second can be quite low!

.. code-block:: console

    $ mysql -u monty -p

.. code-block:: mysql

    mysql> use test_dia;
    mysql> show tables;
    mysql> select * from Metering;



