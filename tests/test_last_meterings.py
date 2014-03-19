#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>

import unittest

import datetime

from station_meteo.last_meterings import LastMeterings


class Test_LastMeterings(unittest.TestCase):
    def setUp(self):
        self.session = 'foobar'
        self.last_meterings = LastMeterings()
        pass
        
    def tearDown(self):
        self.session = None
        self.last_meterings = None  # TODO: know if this is a convenient way
        pass

    def test_parse_raw_string(self):
        self.last_meterings.raw_string = (
            "TEMP,-1,17.40,HUM,-1,57.50,NO2,4236,15.4445400238,CO,125283," +
            "17411.0546875000,VOC,141338,22.7283306121,Dust,2776,0.0003270847" +
            "\n\r")
        a = [
        {'raw': '-1', 'name': 'TEMP', 'value': '17.40'}, 
        {'raw': '-1', 'name': 'HUM', 'value': '57.50'}, 
        {'raw': '4236', 'name': 'NO2', 'value': '15.4445400238'}, 
        {'raw': '125283', 'name': 'CO', 'value': '17411.0546875000'}, 
        {'raw': '141338', 'name': 'VOC', 'value': '22.7283306121'}, 
        {'raw': '2776', 'name': 'Dust', 'value': '0.0003270847'}]
        self.last_meterings.parse_raw_string()
        self.assertEqual(a, self.last_meterings.list)
        pass


