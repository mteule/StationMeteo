#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>

import unittest

import datetime

# TODO: Find a way to catch sqlalchemy.exc.IntegrityError
import sqlalchemy
from sqlalchemy.exc import IntegrityError

from station_meteo.dbms_manager import DBMS_Manager

# TODO: change the sqlalchemy.Engine.bind imported from the model.py file

class Test_DBMS_Manager(unittest.TestCase):
    def setUp(self):
        self.session = 'foobar'
        self.dbms_manager = DBMS_Manager()
        pass
        
    def tearDown(self):
        self.session = None
        self.dbms_manager = None  # TODO: know if this is a convenient way
        pass

    def test_retrieve_sensor_id_dict(self):
        a = {'CO': 3, 'TEMP': 1, 'VOC': 5, 'Dust': 6, 'HUM': 2, 'NO2': 4}
        sensor_id_dict = self.dbms_manager.retrieve_sensor_id_dict()
        self.assertEqual(a, sensor_id_dict)
        pass
        
    def test_insert_metering(self):
        metering = {
            'date': datetime.datetime(2014, 2, 26, 3, 10, 38, 371623),
            'raw': '-1', 'sensor_id': 1, 'name': 'TEMP', 'value': '17.40'}
        # functionnal test:
        self.dbms_manager.insert_metering(metering)
        
        # Raising an Error: #TODO: Maybe needs another function.
        metering = {  # wrong sensor id!
            'date': datetime.datetime(2014, 2, 26, 3, 10, 38, 371623),
            'raw': '-1', 'sensor_id': 77, 'name': 'TEMP', 'value': '17.40'}
        # TODO: pass it into a try catch, it doesn't catch the exception,
        #        maybe because it s raised from another package. 
        # self.assertRaises(
        #     IntegrityError, 
        #     self.dbms_manager.insert_metering(metering))





