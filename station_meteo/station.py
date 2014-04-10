#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>

"""
This is the main module of the package.

It's function "loop()" has to store the meterings data
received from a serial port into a SQL DBMS database.
"""

# TODO: DONE!!! Split attributes into Last_Meterings() and DBMS_Manager()
# TODO: Docstrings
# TODO: nosetest dir ../tests -> tests to have autocode in sphinx
# TODO: Size of strings in the Dia Diagram.
# TODO: Latin-1, utf-8 and db_url: Check the problems we'll may have soon...
#        create_engine('mysql+mysqldb:///mydb?charset=utf8&use_unicode=0')
#        http://docs.sqlalchemy.org/en/rel_0_8/dialects/mysql.html#unicode

import logging
import serial
import time
import datetime
import sqlalchemy

# local modules
import last_meterings
import dbms_manager


class Station (object):
    """
    Connect to each other:
    
    - the Serial port 
    - the string parser "LastMeterings()"
    - the dbms manager "DBMS_Manager()"
    
    Attributes:
    
    :param ser: The RS232 connection to the station's hardware.
    :type ser: :class: `serial.Serial` instance
    :param last_meterings: The string parser
    :type last_meterings: :class: `last_meterings.LastMeterings`
    :param dbms_manager: The connection to the SGBD
    :type dbms_manager: :class: `dbms_manager.DBMS_Manager`
    """
    logger = logging.getLogger(__name__)

    ser = serial.Serial()
    last_meterings = last_meterings.LastMeterings()
    dbms_manager = dbms_manager.DBMS_Manager()

    def __init__(self):
        """"""
        self.ser.port = '/dev/ttyUSB0'
        self.ser.baudrate = 115200
        self.ser.open()
        pass

    def loop(self):
        """"""
        while True:
            self.scan_for_new_data_string()
        pass

    def scan_for_new_data_string(self):
        """"""
        self.last_meterings.raw_string = self.ser.readline()
        if not self.last_meterings.raw_string:
            # must wait for a while
            delay = 1  # seconds
            time.sleep(delay)
        else:
            # store meterings
            self.last_meterings.parse_raw_string()
            self.last_meterings.append_clock(datetime.datetime.now())
            self.last_meterings.sensor_id_dict = \
                self.dbms_manager.retrieve_sensor_id_dict()
            self.last_meterings.append_sensor_id()
            for elem in self.last_meterings.list:
                try:
                    self.dbms_manager.insert_metering(elem)
                except sqlalchemy.exc.IntegrityError as err:
                    # Surely raised if the Sensor table is incomplete
                    self.logger.error(err)

    def _got_meterings_raw_data(self):
        """"""
        self.raw_received_meterings = self.ser.readline()
        # does 'ser.readline()' really try to connect?
        if not 0 == len(self.raw_received_meterings):
            found_new_line = True
        else:
            found_new_line = False
        return found_new_line

if __name__ == "__main__":
        logging.basicConfig(level=logging.DEBUG)
        station = Station()
        station.logger.setLevel("DEBUG")

#        # insert metering value
#        station._insert_metering(
#            {'date': datetime.datetime(2014, 2, 26, 3, 10, 38, 371623),
#            'raw': '-1', 'sensor_id': 1, 'name': 'TEMP', 'value': '17.40'})
#
#        # Exception while inserting metering value
#        print ("Intending to commit a Foreign Key Constraint error:")
#        try:
#            station._insert_metering(
#                {'date': datetime.datetime(2014, 2, 26, 3, 10, 38, 371623),
#                'raw': '-1', 'sensor_id': 77, 'name':
#                'TEMP', 'value': '17.40'})
#        except sqlalchemy.exc.IntegrityError as err:
#            print(err)
