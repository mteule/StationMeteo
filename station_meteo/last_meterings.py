#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>

import logging

# TODO: find a way to get the link in the doc with intersphinx.
 
"""
module used to convert the raw_string received from the serial port into 
a list of dictionnaries. Each dictionnary corresponds to a single sensor 
metering.


"""

class LastMeterings (object):
    """Lets write something to see if it activate intersphinx"""
    
    logger = logging.getLogger(__name__)
    raw_string = ""
    list = list(
            dict({
                'name': 'some_sensor_name',
                'raw': 0,
                'value': 0}))
    sensor_id_dict = dict({
        'name_sensor_1': 'id == 1',
        'name_sensor_2': 'id == 2',
        'name_sensor_3': 'id == 3',
        'name_sensor_4': 'id == 4'})

    def parse_raw_string(self):
        """
        Converts the raw_string to a list of metering dict
        
        The keys of the metering dict are:
        'raw', 'name', 'value'
            
            
        Example of a raw_string:
        >>> last_meterings.raw_string = (
        "TEMP,-1,17.40,HUM,-1,57.50,NO2,4236,15.4445400238,CO,125283," +
        "17411.0546875000,VOC,141338,22.7283306121,Dust,2776,0.0003270847" +
        "\n\r")
            
        What we want to have as an expected behaviour:
        >>> last_meterings.parse_raw_string()
        >>> last_meterings.list
        [{'raw': '-1', 'name': 'TEMP', 'value': '17.40'}, 
        {'raw': '-1', 'name': 'HUM', 'value': '57.50'}, 
        {'raw': '4236', 'name': 'NO2', 'value': '15.4445400238'}, 
        {'raw': '125283', 'name': 'CO', 'value': '17411.0546875000'}, 
        {'raw': '141338', 'name': 'VOC', 'value': '22.7283306121'}, 
        {'raw': '2776', 'name': 'Dust', 'value': '0.0003270847'}]
        
        """
        del(self.list[:])
        data = self.raw_string.rstrip()
        split = [elem.strip() for elem in data.split(',')]
        metering_quantity = len(split) / 3  # 3 params for each sensor

        # Check only the data won't get us into "pointer out of cast" troubles:
        if not (0 == len(split) % metering_quantity):
            raise StandartError("raw data is not consistent")

        # Construct self.list
        metering = dict({'name': 'some_sensor_name', 'raw': 0, 'value': 0})
        for i in range(metering_quantity):
            metering['name'] = split[(i * 3 + 0)]
            metering['raw'] = split[(i * 3 + 1)]
            metering['value'] = split[(i * 3 + 2)]
            self.list.append(metering.copy())

        self.logger.debug("new values for self.list:\n"
            + str(self.list))
        pass

    def append_clock(self, now):
        """
        the 'now' param has to be of the datetime.datetime format to be 
        used latter with sqlalchemy. 
        """
        new_keyval = {'date': now}
        for metering_dict in self.list:
            metering_dict.update(new_keyval)
        pass

    def append_sensor_id(self):
        """
        Appends the sensor id of the metering 
        to each metering dict from the list.

        It uses the data from the sensor_id_dict attribute.
        But this sensor_id_dict has to be refreshed elsewhere.          
        """
        for metering_dict in self.list:
            bus_adress = metering_dict['name']
            new_keyval = {'sensor_id': self.sensor_id_dict[bus_adress]}
            metering_dict.update(new_keyval.copy())
        pass

    pass

