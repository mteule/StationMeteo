#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>

import logging
import serial
import sqlalchemy

class Station (object):
    '''(NULL)'''
    def __init__(self) :
        self.logger = logging.getLogger(__name__) # 
        self.ser = serial.Serial() # 
        self.datab = DatabManager() # 
        self.raw_received_meterings = "" # str
        self.metering_quantity = 0 # int
        self.last_meterings_list = list() # 
        self.sensor_dict = dict('id': ,'name': ) # 
        pass

    def setup (self) :
        self.ser.port = '/dev/ttyUSB0'
        self.ser.baudrate = 115200
        self.ser.open()
        pass
        
    def loop (self) :
        if  _get_meterings_raw_data():
             # refresh datab and sensor_dict:
             datab.session.connect #?
             self.sensor_dict = 
             
             _parse_raw_data()
             
             for metering in self.last_meterings_list:
                 try:
                     datab.session.add(metering)
                 except Error() as err:
                     self.logger.ERROR(err)
        pass

    def _get_meterings_raw_data (self) :
        self.raw_received_meterings = self.ser.readline()
        if not 0==len(self.raw_received_meterings)
            return True
        else:
            return False
        pass

    def _parse_raw_data (self) :
        self.raw_received_meterings = "" # str
        self.metering_quantity = 0 # int
        self.last_meterings_list = list() # 
        # returns 
        pass
    def _store_meterings (self) :
         for metering in self.last_meterings_list:
             try:
                 datab.session.add(metering)
             except Error() as err:
                 self.logger.ERROR(err)
        pass

