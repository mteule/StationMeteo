#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>

import unittest

import datetime

# TODO: Find a way to catch sqlalchemy.exc.IntegrityError
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
        # TODO: check if this is a convenient way to destroy an object:
        self.dbms_manager = None  
        pass

    def test_retrieve_sensor_id_dict(self):
        """
        Test the function with a constant "a" sensor_id_dict.
        If the default sensor database changes this must be fixed 
        """
        a = {'CO': 3, 'TEMP': 1, 'VOC': 5, 'Dust': 6, 'HUM': 2, 'NO2': 4}
        sensor_id_dict = self.dbms_manager.retrieve_sensor_id_dict()
        self.assertEqual(a, sensor_id_dict)
        pass

    def test_insert_metering(self):
        # FIRST PART
        # (simple functionnal test)
        # Using a valid metering dict() value:
        metering = {
            'date': datetime.datetime(2014, 2, 26, 3, 10, 38, 371623),
            'raw': '-1', 'sensor_id': 1, 'name': 'TEMP', 'value': '17.40'}
        self.dbms_manager.insert_metering(metering)

        # SECOND PART: Raising an IntegrityError
        # TODO: Maybe needs another function.
        # Using an inappropriate metering dict, with an incorrect sensor_id value
        metering = {  # wrong sensor_id = 77!
            'date': datetime.datetime(2014, 2, 26, 3, 10, 38, 371623),
            'raw': '-1', 'sensor_id': 77, 'name': 'TEMP', 'value': '17.40'}
        self.assertRaises(
            IntegrityError,
            self.dbms_manager.insert_metering,
            metering)
