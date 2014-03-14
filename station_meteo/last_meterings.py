#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>

class LastMeterings (object):

    raw_string = ""  # str
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

    def _parse_raw_string(self):
        """"""
        del(self.last_meterings_list[:])
        data = self.raw_string.rstrip()
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

    def _append_clock(self, now):
        """"""
        new_keyval = {'date': now}
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

    pass

