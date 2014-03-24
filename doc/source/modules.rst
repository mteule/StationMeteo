Modules:
========

station_meteo.station
---------------------

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
>>> stat.loop_new()

$ mysql -u monty -p

mysql> use test_dia;
mysql> show tables;
mysql> select * from Metering;

.. automodule:: station_meteo.station
   :members:
   :undoc-members:

station_meteo.last_meterings
----------------------------

>>> import last_meterings
>>> last_m = last_meterings.LastMeterings()
>>> last_m.raw_string = (
            "TEMP,-1,17.40,HUM,-1,57.50,NO2,4236,15.4445400238,CO,125283," +
            "17411.0546875000,VOC,141338,22.7283306121,Dust,2776,0.0003270847" +
            "\n\r")
>>> last_m.list
['raw', 'name', 'value']
>>> last_m.parse_raw_string()
>>> last_m.list
[{'raw': '-1', 'name': 'TEMP', 'value': '17.40'}, {'raw': '-1', 'name': 'HUM', 'value': '57.50'}, {'raw': '4236', 'name': 'NO
2', 'value': '15.4445400238'}, {'raw': '125283', 'name': 'CO', 'value': '17411.0546875000'}, {'raw': '141338', 'name': 'VOC',
 'value': '22.7283306121'}, {'raw': '2776', 'name': 'Dust', 'value': '0.0003270847'}]
>>> import datetime
>>> last_m.append_clock(datetime.datetime.now())
>>> last_m.list
[{'date': datetime.datetime(2014, 3, 24, 15, 15, 27, 806922), 'raw': '-1', 'name': 'TEMP', 'value': '17.40'}, {'date': dateti
me.datetime(2014, 3, 24, 15, 15, 27, 806922), 'raw': '-1', 'name': 'HUM', 'value': '57.50'}, {'date': datetime.datetime(2014,
 3, 24, 15, 15, 27, 806922), 'raw': '4236', 'name': 'NO2', 'value': '15.4445400238'}, {'date': datetime.datetime(2014, 3, 24,
 15, 15, 27, 806922), 'raw': '125283', 'name': 'CO', 'value': '17411.0546875000'}, {'date': datetime.datetime(2014, 3, 24, 15
, 15, 27, 806922), 'raw': '141338', 'name': 'VOC', 'value': '22.7283306121'}, {'date': datetime.datetime(2014, 3, 24, 15, 15,
 27, 806922), 'raw': '2776', 'name': 'Dust', 'value': '0.0003270847'}]
>>> last_m.sensor_id_dict = {'CO': 3, 'TEMP': 1, 'VOC': 5, 'Dust': 6, 'HUM': 2, 'NO2': 4}
>>> last_m.append_sensor_id()
>>> last_m.list
[{'date': datetime.datetime(2014, 3, 24, 15, 15, 27, 806922), 'raw': '-1', 'sensor_id': 1, 'name': 'TEMP', 'value': '17.40'},
 {'date': datetime.datetime(2014, 3, 24, 15, 15, 27, 806922), 'raw': '-1', 'sensor_id': 2, 'name': 'HUM', 'value': '57.50'},
{'date': datetime.datetime(2014, 3, 24, 15, 15, 27, 806922), 'raw': '4236', 'sensor_id': 4, 'name': 'NO2', 'value': '15.44454
00238'}, {'date': datetime.datetime(2014, 3, 24, 15, 15, 27, 806922), 'raw': '125283', 'sensor_id': 3, 'name': 'CO', 'value':
 '17411.0546875000'}, {'date': datetime.datetime(2014, 3, 24, 15, 15, 27, 806922), 'raw': '141338', 'sensor_id': 5, 'name': '
VOC', 'value': '22.7283306121'}, {'date': datetime.datetime(2014, 3, 24, 15, 15, 27, 806922), 'raw': '2776', 'sensor_id': 6,
'name': 'Dust', 'value': '0.0003270847'}]


.. automodule:: station_meteo.last_meterings
   :members:
   :undoc-members:
   
station_meteo.dbms_manager
--------------------------

>>> import dbms_manager
>>> dbms_manager = dbms_manager.DBMS_Manager()
>>> sensor_id_dict = dbms_manager.retrieve_sensor_id_dict()
>>> sensor_id_dict
{'CO': 3, 'TEMP': 1, 'VOC': 5, 'Dust': 6, 'HUM': 2, 'NO2': 4}
>>> 


.. automodule:: station_meteo.dbms_manager
   :members:
   :undoc-members:

station_meteo.model
-------------------

.. automodule:: station_meteo.model
   :members:
   :undoc-members:
   :private-members:
