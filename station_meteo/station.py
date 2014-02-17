#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>

import logging
import serial
import time

from model import *

# may not be so usefull, seems that model will be totally sufficient
from datab import *


class Station (object):
    '''(NULL)'''

    logger = logging.getLogger(__name__)

    clock = None  # TODO: make it to have the 'date' value to insert
    raw_received_meterings = ("")  # str
    metering_quantity = 0  # int
    ser = None  # serial.Serial()

    def __init__(self):
        self.ser = serial.Serial()
        self.datab = DatabManager()
        self.last_meterings_list = list(
            dict({'name': 'some_sensor_name', 'raw': 0, 'value': 0}))
        self.sensor_id_dict = dict({'name': 'id'})
        pass

    def setup_ser(self, port='/dev/ttyUSB0', baudrate=115200):
        # TODO: change, this is ugly.
        self.ser = serial.Serial(port=port, baudrate=baudrate)
        self.ser.open()
        pass

    def loop(self):
        if  self._get_meterings_raw_data():
            self.store_meterings()
        else:
            # wait for a while
            delay = 1  # seconds
            time.sleep(delay)
        pass

    def store_meterings(self):
        self._parse_raw_data()

        # date value data
        self._refresh_clock()
        self._append_clock()

        # refresh datab "is the db alive?"
        # datab.session.connect()

        self._refresh_sensor_id_dict()  # May itself test the db
        self._append_sensor_id()
        self._store_in_db()
        pass

    def _refresh_clock(self):
        # TODO:
        pass

    def _append_clock(self):
        # TODO:
        pass

    def _refresh_sensor_id_dict(self):
        # TODO: refresh from a sqlalchemy select
        # mysql> select id, bus_adress from Sensor
        self.sensor_id_dict.clear()
        self.sensor_id_dict = {
            'TEMP': 1,
            'HUM': 2,
            'CO': 3,
            'NO2': 4,
            'VOC': 5,
            'Dust': 6}
        pass

    def _append_sensor_id(self):
        # TODO:
        for metering_dict in self.last_meterings_list:
            bus_adress = metering_dict['name']
            new = {'sensor_id': self.sensor_id_dict[bus_adress]}
            metering_dict.update(new)
        pass

    def _get_meterings_raw_data(self):
        self.raw_received_meterings = self.ser.readline()
        # try connect?
        if not 0 == len(self.raw_received_meterings):
            found_new_line = True
        else:
            found_new_line = False
        return found_new_line

    def _parse_raw_data(self):
        del(self.last_meterings_list[:])
        data = self.raw_received_meterings.rstrip()
        split = [elem.strip() for elem in data.split(',')]
        metering_quantity = len(split) / 3

        # Check only the data won't get us into "pointer out of cast" troubles:
        if not (0 == len(split) % metering_quantity):
            raise StandartError("raw data is not consistent")

        metering = dict({'name': 'some_sensor_name', 'raw': 0, 'value': 0})
        for i in range(metering_quantity):
            metering['name'] = split[(i * 3 + 0)]
            metering['raw'] = split[(i * 3 + 1)]
            metering['value'] = split[(i * 3 + 2)]
            self.last_meterings_list.append(metering.copy())

        self.logger.debug("new values for self.last_meterings_list:\n"
            + str(self.last_meterings_list))
        pass

    def _store_in_db(self):
        # http://pylonsbook.com/en/1.1/introducing-the-model-and-sqlalchemy.html#sql-expression-api
        # meter = Metering()
        # meter.__table__ *may*/can? be used as page_table in the documentation:
        # ins = meter.__table__.insert(values=dict(name=u'test', title=u'Test Page', content=u'Some content!'))
        for elem in self.last_meterings_list:
            # append the right sensor_id
            next_insert = Metering()  # next row? row?
            next_insert.sensor_id = elem['sensor_id']
            next_insert.raw = elem['raw']
            next_insert.value = elem['value']
            datab.session.add(next_insert)
            try:
                datab.session.commit()
            except Error() as err:
                self.logger.error(err)
        pass
pass

if __name__ == "__main__":
        logging.basicConfig(level=logging.DEBUG)
        station = Station()
        station.logger.setLevel("DEBUG")

        logging.debug("Testing station.raw_received_meterings()")
        station.raw_received_meterings = (
            "TEMP,-1,17.40,HUM,-1,57.50,NO2,4236,15.4445400238,CO,125283," +
            "17411.0546875000,VOC,141338,22.7283306121,Dust,2776,0.0003270847" +
            "\n\r")
        station._parse_raw_data()
        #Check that old meterings where del():
        station._parse_raw_data()

        # Sensor_id
        print "Test sensor_id"
        print station.sensor_id_dict
        station._refresh_sensor_id_dict()
        print station.sensor_id_dict
        station._append_sensor_id()
        print "updated metering list"
        print station.last_meterings_list

