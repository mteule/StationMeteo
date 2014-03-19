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

