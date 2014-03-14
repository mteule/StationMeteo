#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>

import sqlalchemy
from model import Sensor, Metering


# moved here to use a RAW 'sqlacodegen' generated model.py
db_url = 'mysql://monty:passwd@localhost/test_dia'
engine = sqlalchemy.create_engine(db_url)
metadata.bind = engine


class DBMS_Manager (object):

    # DBMS connection:
    sensor_table = Sensor().__table__
    metering_table = Metering().__table__

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
pass

