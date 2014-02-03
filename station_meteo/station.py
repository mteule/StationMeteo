#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>

import logging
import serial

from model import *

class Station (object):
    '''(NULL)'''
    def __init__(self) :
        self.logger = logging.getLogger(__name__) # 
        self.ser = serial.Serial() # 
        self.datab = DatabManager() # 
        self.raw_received_meterings = "" # str
        self.metering_quantity = 0 # int
        self.last_meterings_list = list() # 
        self.sensor_dict = dict({'id':"" ,'name':""}) # 
        pass

    def setup (self) :
        self.ser.port = '/dev/ttyUSB0'
        self.ser.baudrate = 115200
        self.ser.open()
        pass
        
    def loop (self) :
        if  _get_meterings_raw_data():
            # ----- STORE IN DATABASE ----- #
             # refresh datab and sensor_dict:
             datab.session.connect # ? is the db alive?
             # refresh sensors_dict() ?
             self.sensor_dict = {} # refresh the dict({'name', 'id'}) from the database. sensor_dict Must be an attribute.
             
             _parse_raw_data()
             _store_meterings (self)             
        pass

    def _get_meterings_raw_data (self) :
        self.raw_received_meterings = self.ser.readline()
        # try connect?
        if not 0==len(self.raw_received_meterings):
            return True
        else:
            return False
        pass

    def _parse_raw_data (self, raw_received_meterings=""):
        data = raw_received_meterings.rstrip() 
        split = [elem.strip() for elem in data.split(',')]
        metering_quantity = len(split) / 3
        # Check only the data won't get us into "pointer out of cast" troubles:
        if not (0 == len(split) % metering_quantity):
        	raise StandartError("raw data is not consistent")
    	
        metering = dict({'name': 'some_sensor_name', 'raw': 0, 'value': 0})
        last_meterings_list = list()
        for i in range (0, metering_quantity):
            metering ['name'] = split[(i*3 + 0)]
            metering ['raw'] = split[(i*3 + 1)]
            metering ['value'] = split[(i*3 + 2)]
            last_meterings_list.append(metering)
        return last_meterings_list

    def _store_meterings (self) :
        for elem in self.last_meterings_list:
            # append the right sensor_id
            next_insert = Metering() # next row? row?
            next_insert.sensor_id=elem['sensor_id']
            next_insert.raw=elem['raw'] 
            next_insert.value=elem['value']
            datab.session.add(next_insert)
            try:
                datab.session.commit()
            except Error() as err:
                self.logger.error(err)
        pass

