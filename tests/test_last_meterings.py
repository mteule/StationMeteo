
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
