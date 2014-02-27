StationMeteo
============

Scripts aiming at using the little serial meteo station.

Context:
--------

The :meteo station: will send every 5 minutes a string on the serial port /dev/ttyUSB0.
This strings contains the raw value and the 'readable' value for a set of 6 air quality sensors.

Each of these meterings will have to be stored in a database.

Specifications:
===============

station.raw_received_meterings:
-------------------------------
The strings red from the serial port would be of this kind:

    raw_received_meterings = (
            "TEMP,-1,17.40,HUM,-1,57.50,NO2,4236,15.4445400238,CO,125283," +
            "17411.0546875000,VOC,141338,22.7283306121,Dust,2776,0.0003270847" +
            "\n\r")
            
station.last_meterings_list, station._parse_raw_data():
-------------------------------------------------------
The above string will have to be parsed to obtain a list of dictionnaries.
Each dictionnary corresponds to a metering.

    >>> station._parse_raw_data()
    >>> station.last_meterings_list
    [{'raw': '-1', 'name': 'TEMP', 'value': '17.40'}, 
    {'raw': '-1', 'name': 'HUM', 'value': '57.50'}, 
    {'raw': '4236', 'name': 'NO2', 'value': '15.4445400238'}, 
    {'raw': '125283', 'name': 'CO', 'value': '17411.0546875000'}, 
    {'raw': '141338', 'name': 'VOC', 'value': '22.7283306121'}, 
    {'raw': '2776', 'name': 'Dust', 'value': '0.0003270847'}]

station.sensor_id_dict & station.clock.now():
---------------------------------------------
To insert the meterings in the database, for each metering we need to replace the sensor's name by the value of the sensor_id in the database. 
The list of the sensor_id is retrieved from the database rather than being written in the code.

It is of this form:
    >>> station._refresh_sensor_id_dict()
    >>> station.sensor_id_dict
    {'CO': 3, 'TEMP': 1, 'VOC': 5, 'Dust': 6, 'HUM': 2, 'NO2': 4}

We also have to insert in the database a datetime for each metering.
The same value for a whole raw_meterings string.

We therefore append these values to each metering dictionnary of the list:

    >>> station._append_sensor_id()
    >>> station._append_clock()
    >>> station.last_meterings_list
    [{'date': datetime.datetime(2014, 2, 27, 5, 59, 28, 262085), 
        'raw': '-1','sensor_id': 1, 'name': 'TEMP', 'value': '17.40'}, 
    {'date': datetime.datetime(2014, 2, 27, 5, 59, 28, 262085), 
        'raw': '-1', 'sensor_id': 2, 'name': 'HUM', 'value': '57.50'}, 
    {'date': datetime.datetime(2014, 2, 27, 5, 59, 28, 262085), 
        'raw': '4236', 'sensor_id': 4, 'name': 'NO2', 'value': '15.4445400238'},
    {'date': datetime.datetime(2014, 2, 27, 5, 59, 28, 262085), 
        'raw': '125283', 'sensor_id': 3, 'name': 'CO', 'value': '17411.0546875000'},
    {'date': datetime.datetime(2014, 2, 27, 5, 59, 28, 262085), 
        'raw': '141338', 'sensor_id': 5, 'name': 'VOC', 'value': '22.7283306121'},
    {'date': datetime.datetime(2014, 2, 27, 5, 59, 28, 262085), 
        'raw': '2776', 'sensor_id': 6, 'name': 'Dust', 'value': '0.0003270847'}]

station._store_in_db():
-----------------------
We store each of the metering dict() in the database.
Using station._insert_metering()


