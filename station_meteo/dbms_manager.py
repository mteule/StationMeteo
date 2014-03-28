#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>

import logging
import sqlalchemy

from model import Sensor, Metering, metadata

"""
This dbms_manager module will be used to interact with databases.

It is separated from, but uses, the sqlalchemy declarative model,
 imported as model.py.

It initializes the globals values of the declarative model

"""

# moved here to use a RAW 'sqlacodegen' generated model.py
db_url = 'mysql://monty:passwd@localhost/test_dia'
engine = sqlalchemy.create_engine(db_url)
metadata.bind = engine


class DBMS_Manager (object):
    """
    Standart object used to gather all the operation on the DBMS.
    """
    logger = logging.getLogger(__name__)

    # DBMS connection:
    sensor_table = Sensor().__table__
    metering_table = Metering().__table__

    def retrieve_sensor_id_dict(self):
        """
        Retrieve a sensor_id_dict from the database.
        The reference of the dict is given as the return value.

        It's content corresponds to a simple select, for example with mysql:
            mysql> select id, bus_adress from Sensor;

        the returned dict has to look like this:

        {'CO': 3, 'TEMP': 1, 'VOC': 5, 'Dust': 6, 'HUM': 2, 'NO2': 4}
        """

        sensor_id_dict = dict()
        sel = sqlalchemy.select([
            self.sensor_table.c.bus_adress,
            self.sensor_table.c.id])
        res = sel.execute()
        for row in res:
            # Strange but 'id' is received as "type(id)==long"?!?
            new_keyval = {
                row[self.sensor_table.c.bus_adress]:
                int(row[self.sensor_table.c.id])}
            sensor_id_dict.update(new_keyval.copy())
            # type(new_keyval) == dict() with only one key
        return sensor_id_dict

    def insert_metering(self, meterings={}):
        """
        Simply use the sqlalchemy DBMS connection
        to insert the values of a metering.
        The metering values are passed as a simple dict().

        For example:

            {'date': datetime.datetime(2014, 2, 27, 5, 59, 28, 262085),
            'raw': '-1', 'sensor_id': 2, 'name': 'HUM', 'value': '57.50'}

        The only keys that will be inserted will be:

            meterings['value'],
            meterings['date'],
            meterings['raw'],
            meterings['sensor_id']
        """
        ins = self.metering_table.insert().values(
            value=meterings['value'],
            datetime=meterings['date'],
            raw=meterings['raw'],
            sensor_id=meterings['sensor_id'])
        # .'compile().params' is usefull for debug,
        #        but anyway it would be done automatically when executing
        ins_string = ins.compile().params
        ins.execute()
        self.logger.debug(ins_string)
        pass
pass

if __name__ == "__main__":
        import datetime

        logging.basicConfig(level=logging.DEBUG)
        dbms_manager = DBMS_Manager()
        dbms_manager.logger.setLevel("DEBUG")

        # functionnal test:
        metering = {
            'date': datetime.datetime(2014, 2, 26, 3, 10, 38, 371623),
            'raw': '-1', 'sensor_id': 1, 'name': 'TEMP', 'value': '17.40'}

        dbms_manager.insert_metering(metering)

        # Raising an Error: #TODO: Maybe needs another function.
        metering = {  # wrong sensor id!
            'date': datetime.datetime(2014, 2, 26, 3, 10, 38, 371623),
            'raw': '-1', 'sensor_id': 77, 'name': 'TEMP', 'value': '17.40'}

        dbms_manager.insert_metering(metering)