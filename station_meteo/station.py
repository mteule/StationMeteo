#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>

"""
This is the main module of the package.

It's function "loop()" has to store the meterings data received from a serial port into a SQL DBMS database.
"""

# TODO: Split attributes into Last_Meterings() and DBMS_Manager()
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

from model import *

# TODO: rm, moved to DBMS_Manager()
# moved here to use a RAW 'sqlacodegen' generated model.py
db_url = 'mysql://monty:passwd@localhost/test_dia'
engine = sqlalchemy.create_engine(db_url)
metadata.bind = engine


class Station (object):
    """
    Connect the Serial port to the string parser "LastMeterings()" and the dbms manager "DBMS_Manager()" 

    """

    logger = logging.getLogger(__name__)

    clock = datetime.datetime
    ser = serial.Serial()

    # TODO: rm, moved to DBMS_Manager()
    # DBMS connection:
    sensor_table = Sensor().__table__
    metering_table = Metering().__table__

    # TODO: remove all this part when it is switched towards LastMeterings()
    # "Serial Inputted/Parsed" datas
    raw_received_meterings = ""  # str
    last_meterings_list = list(
            dict({
                'name': 'some_sensor_name',
                'raw': 0,
                'value': 0}))
    sensor_id_dict = dict({
        'name_sensor_1': 'id == 1',
        'name_sensor_2': 'id == 2',
        'name_sensor_3': 'id == 3',
        'name_sensor_4': 'id == 4'})

    def __init__(self):
        """"""
        # TODO: when ../test dir is functionnal,
        #        move here our setup of serial.Serial()
        pass

    def loop(self):
        """"""
        self.ser.port = '/dev/ttyUSB0'
        self.ser.baudrate = 115200
        self.ser.open()

        while True:
            if not self._got_meterings_raw_data():
                # must wait for a while
                delay = 1  # seconds
                time.sleep(delay)
            else:
                # store meterings
                self._parse_raw_data()
                self._append_clock(self.clock.now())
                self._refresh_sensor_id_dict()
                self._append_sensor_id()
                for elem in self.last_meterings_list:
                    try:
                        self._insert_metering(elem)
                    except sqlalchemy.exc.IntegrityError as err:
                        # Surely raised if the Sensor table is incomplete
                        self.logger.error(err)
        pass

    # TODO: rm, moved to DBMS_Manager()
    def _refresh_sensor_id_dict(self):
        """"""
        # mysql> select id, bus_adress from Sensor
        self.sensor_id_dict.clear()
        sel = sqlalchemy.select([
            self.sensor_table.c.bus_adress,
            self.sensor_table.c.id])
        res = sel.execute()
        for row in res:
            # Strange but 'id' is received as "type(id)==long"?!?
            new_keyval = {
                row[self.sensor_table.c.bus_adress]:
                int(row[self.sensor_table.c.id])}
            self.sensor_id_dict.update(new_keyval.copy())
            # type(new_keyval) == dict() with only one key
        pass

    # TODO: rm, moved to LastMeterings()
    def _append_clock(self, now):
        """"""
        new_keyval = {'date': now}
        for metering_dict in self.last_meterings_list:
            metering_dict.update(new_keyval)
        pass

    # TODO: rm, moved to LastMeterings()
    def _append_sensor_id(self):
        """"""
        for metering_dict in self.last_meterings_list:
            bus_adress = metering_dict['name']
            new_keyval = {'sensor_id': self.sensor_id_dict[bus_adress]}
            metering_dict.update(new_keyval.copy())
        pass

    def _got_meterings_raw_data(self):
        """"""
        self.raw_received_meterings = self.ser.readline()
        # does 'ser.readline()' really try to connect?
        if not 0 == len(self.raw_received_meterings):
            found_new_line = True
        else:
            found_new_line = False
        return found_new_line

    # TODO: rm, moved to LastMeterings()
    def _parse_raw_data(self):
        """"""
        del(self.last_meterings_list[:])
        data = self.raw_received_meterings.rstrip()
        split = [elem.strip() for elem in data.split(',')]
        metering_quantity = len(split) / 3  # 3 params for each sensor

        # Check only the data won't get us into "pointer out of cast" troubles:
        if not (0 == len(split) % metering_quantity):
            raise StandartError("raw data is not consistent")

        # Construct self.last_meterings_list
        metering = dict({'name': 'some_sensor_name', 'raw': 0, 'value': 0})
        for i in range(metering_quantity):
            metering['name'] = split[(i * 3 + 0)]
            metering['raw'] = split[(i * 3 + 1)]
            metering['value'] = split[(i * 3 + 2)]
            self.last_meterings_list.append(metering.copy())

        self.logger.debug("new values for self.last_meterings_list:\n"
            + str(self.last_meterings_list))
        pass
    # TODO: rm, moved to DBMS_Manager()
    def _insert_metering(self, meterings={}):
        """"""
        ins = self.metering_table.insert().values(
            value=meterings['value'],
            datetime=meterings['date'],
            raw=meterings['raw'],
            sensor_id=meterings['sensor_id'])
        # .'compile().params' is usefull for debug,
        #        but anyway it would be done automatically when executing
        ins.compile().params
        ins.execute()
        # self.logger.debug(ins)
pass

if __name__ == "__main__":
        logging.basicConfig(level=logging.DEBUG)
        station = Station()
        station.logger.setLevel("DEBUG")

        # insert metering value
        station._insert_metering(
            {'date': datetime.datetime(2014, 2, 26, 3, 10, 38, 371623),
            'raw': '-1', 'sensor_id': 1, 'name': 'TEMP', 'value': '17.40'})

        # Exception while inserting metering value
        print ("Intending to commit a Foreign Key Constraint error:")
        try:
            station._insert_metering(
                {'date': datetime.datetime(2014, 2, 26, 3, 10, 38, 371623),
                'raw': '-1', 'sensor_id': 77, 'name': 'TEMP', 'value': '17.40'})
        except sqlalchemy.exc.IntegrityError as err:
            print(err)

