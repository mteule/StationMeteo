#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>

class Station :
    '''(NULL)'''
    def __init__(self) :
        self.logger = logging.getLogger(__name__) # 
        self.ser = serial.Serial() # 
        self.parser = InputParser() # 
        self.datab = DatabManager() # 
        self.raw_received_meterings = "" # str
        self.metering_quantity = 0 # int
        self.last_meterings_list = list() # 
        self.sensor_dict = dict('id': ,'name': ) # 
        pass
    def _get_meterings_raw_data (self) :
        # returns 
        pass
    def _parse_raw_data (self) :
        # returns 
        pass
    def _store_meterings (self) :
        # returns 
        pass
    def setup (self) :
        # returns 
        pass
    def loop (self) :
        # returns 
        pass
