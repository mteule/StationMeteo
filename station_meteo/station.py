#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>

import logging
import serial
import time
import datetime
import sqlalchemy

from model import *

# moved here to use 'sqlacodegen' generated model.py
db_url = 'mysql://monty:passwd@localhost/test_dia'
engine = sqlalchemy.create_engine(db_url)
metadata.bind = engine


class Station (object):
    '''(NULL)'''

    logger = logging.getLogger(__name__)

    clock = datetime.datetime
    raw_received_meterings = ""  # str
    ser = serial.Serial()

    # TODO: pass to metering_tbl et sensor_table
    sensor = Sensor()
    metering = Metering()

    def __init__(self):
        self.last_meterings_list = list(
            dict({'name': 'some_sensor_name', 'raw': 0, 'value': 0}))
        self.sensor_id_dict = dict({'name': 'id'})
        pass

    def loop(self):

        self.ser.port = '/dev/ttyUSB0'
        self.ser.baudrate = 115200
        self.ser.open()

        while True:
            if not self._got_meterings_raw_data():  # must wait for a while
                delay = 1  # seconds
                time.sleep(delay)
            else:  # store meterings
                # TODO: copy content of store_meterings here
                # when /test dir construction is achieved.
                # Anyway this store_meterings function is quite usefull,
                # we may keep it
                self.store_meterings()
        pass

    def store_meterings(self):
        """ """
        self._parse_raw_data()
        self._append_clock()
        self._refresh_sensor_id_dict()  # By itself test the db connection
        self._append_sensor_id()
        self._store_in_db()
        pass

    def _refresh_sensor_id_dict(self):
        """"""
        # mysql> select id, bus_adress from Sensor
        self.sensor_id_dict.clear()
        sens_table = self.sensor.__table__
        sel = sqlalchemy.select([sens_table.c.bus_adress, sens_table.c.id])
        res = sel.execute()
        for row in res:
            # Strange but 'id' is received as "type(id)==long"?!?
            new_keyval = {
                row[sens_table.c.bus_adress]: int(row[sens_table.c.id])}
            self.sensor_id_dict.update(new_keyval.copy())
        pass

    def _append_clock(self):
        """"""
        new_keyval = {'date': self.clock.now()}
        for metering_dict in self.last_meterings_list:
            metering_dict.update(new_keyval)
        pass

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
        # try connect?
        if not 0 == len(self.raw_received_meterings):
            found_new_line = True
        else:
            found_new_line = False
        return found_new_line

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

    def _insert_metering(self, meterings={}):
        """"""
        meter_table = self.metering.__table__
        ins = meter_table.insert().values(
            value=meterings['value'],
            datetime=meterings['date'],
            raw=meterings['raw'],  # TODO: Correct first the Dia Diagramm
            sensor_id=meterings['sensor_id'])
        ins.compile().params  # no usefull, done automatically by executing
        ins.execute()
        self.logger.debug(ins)

    def _store_in_db(self):
        """"""
        for elem in self.last_meterings_list:
            try:
                self._insert_metering(elem)
            except sqlalchemy.exc.IntegrityError as err:
                # Surely raised if the Sensor table is incomplete
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

        # append clock and Sensor_id
        print ("\nTest sensor_id")
        print ((station.sensor_id_dict))
        station._refresh_sensor_id_dict()
        print ((station.sensor_id_dict))

        station._append_sensor_id()
        print (("\nsensor_id updated metering list:"))
        print ((station.last_meterings_list))

        station._append_clock()
        print ("\nclock updated metering list:")
        print ((station.last_meterings_list))

        # insert metering value
        station._insert_metering(
            {'date': datetime.datetime(2014, 2, 26, 3, 10, 38, 371623),
            'raw': '-1', 'sensor_id': 1, 'name': 'TEMP', 'value': '17.40'})

        # Inserting whole list of meterings
        station._store_in_db()

        # Exception while inserting metering value
        try:
            station._insert_metering(
                {'date': datetime.datetime(2014, 2, 26, 3, 10, 38, 371623),
                'raw': '-1', 'sensor_id': 77, 'name': 'TEMP', 'value': '17.40'})
        except sqlalchemy.exc.IntegrityError as err:
            print ("Intending to commit a Foreign Key Constraint error:")
            print(err)

        station.last_meterings_list[4]['sensor_id'] = 77
        station._store_in_db()