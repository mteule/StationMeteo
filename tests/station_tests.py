import unittest

import datetime
import sqlalchemy
from sqlalchemy.exc import IntegrityError

from station_meteo.station import Station

class MyTest(unittest.TestCase):
    def setUp(self):
        self.session = 'foobar'
        self.station = Station()
        self.station.raw_received_meterings = (
            "TEMP,-1,17.40,HUM,-1,57.50,NO2,4236,15.4445400238,CO,125283," +
            "17411.0546875000,VOC,141338,22.7283306121,Dust,2776,0.0003270847" +
            "\n\r")
        pass
        
    def tearDown(self):
        self.session = None
        self.station  # TODO: know if a close() function is necessary
        pass

    def test__parse_raw_data(self):
        a = [  # List
        {'raw': '-1', 'name': 'TEMP', 'value': '17.40'}, 
        {'raw': '-1', 'name': 'HUM', 'value': '57.50'}, 
        {'raw': '4236', 'name': 'NO2', 'value': '15.4445400238'}, 
        {'raw': '125283', 'name': 'CO', 'value': '17411.0546875000'}, 
        {'raw': '141338', 'name': 'VOC', 'value': '22.7283306121'}, 
        {'raw': '2776', 'name': 'Dust', 'value': '0.0003270847'}]
        self.station._parse_raw_data()
        self.assertEqual(a, self.station.last_meterings_list)
        pass

    def test__refresh_sensor_id_dict(self):
        a = {'CO': 3, 'TEMP': 1, 'VOC': 5, 'Dust': 6, 'HUM': 2, 'NO2': 4}
        self.station._refresh_sensor_id_dict()
        self.assertEqual(a, self.station.sensor_id_dict)
        pass 
               
    def test__append_sensor_id(self):
        a = [
        {'raw': '-1', 'sensor_id': 1, 'name': 'TEMP', 'value': '17.40'}, 
        {'raw': '-1', 'sensor_id': 2, 'name': 'HUM', 'value': '57.50'}, 
        {'raw': '4236', 'sensor_id': 4, 'name': 'NO2', 'value': '15.4445400238'}, 
        {'raw': '125283', 'sensor_id': 3, 'name': 'CO', 'value': '17411.0546875000'}, 
        {'raw': '141338', 'sensor_id': 5, 'name': 'VOC', 'value': '22.7283306121'}, 
        {'raw': '2776', 'sensor_id': 6, 'name': 'Dust', 'value': '0.0003270847'}]
        self.station.sensor_id_dict = {'CO': 3, 'TEMP': 1, 'VOC': 5, 'Dust': 6, 'HUM': 2, 'NO2': 4}
        self.station._parse_raw_data()  # TODO: see if this is too functional 
        self.station._append_sensor_id()
        self.assertEqual(a, self.station.last_meterings_list)        
        pass
                
    def test__append_clock(self):
        a = [
    {'date': datetime.datetime(2014, 2, 27, 5, 59, 28, 262085), 
    'raw': '-1','sensor_id': 1, 'name': 'TEMP', 'value': '17.40'}, 
    {'date': datetime.datetime(2014, 2, 27, 5, 59, 28, 262085), 
    'raw': '-1', 'sensor_id': 2, 'name': 'HUM', 'value': '57.50'}, 
    {'date': datetime.datetime(2014, 2, 27, 5, 59, 28, 262085), 
    'raw': '4236', 'sensor_id': 4, 'name': 'NO2', 'value': '15.4445400238'},
    {'date': datetime.datetime(2014, 2, 27, 5, 59, 28, 262085), 
    'raw': '125283', 'sensor_id': 3, 'name': 'CO', 'value': '17411.0546875000'},
    {'date': datetime.datetime(2014, 2, 27, 5, 59, 28, 262085), 
    'raw': '141338', 'sensor_id': 5, 'name': 'VOC', 'value': '22.7283306121'},
    {'date': datetime.datetime(2014, 2, 27, 5, 59, 28, 262085), 
    'raw': '2776', 'sensor_id': 6, 'name': 'Dust', 'value': '0.0003270847'}]
        self.station.last_meterings_list = [
        {'raw': '-1', 'sensor_id': 1, 'name': 'TEMP', 'value': '17.40'}, 
        {'raw': '-1', 'sensor_id': 2, 'name': 'HUM', 'value': '57.50'}, 
        {'raw': '4236', 'sensor_id': 4, 'name': 'NO2', 'value': '15.4445400238'}, 
        {'raw': '125283', 'sensor_id': 3, 'name': 'CO', 'value': '17411.0546875000'}, 
        {'raw': '141338', 'sensor_id': 5, 'name': 'VOC', 'value': '22.7283306121'}, 
        {'raw': '2776', 'sensor_id': 6, 'name': 'Dust', 'value': '0.0003270847'}]
        self.station._append_clock(
            self.station.clock(2014, 2, 27, 5, 59, 28, 262085))
        self.assertEqual(a, self.station.last_meterings_list)        
        pass
        
    def test__insert_metering(self):
        metering = {
            'date': datetime.datetime(2014, 2, 26, 3, 10, 38, 371623),
            'raw': '-1', 'sensor_id': 1, 'name': 'TEMP', 'value': '17.40'}
        self.station._insert_metering(metering)
        metering = {  # wrong sensor id!
            'date': datetime.datetime(2014, 2, 26, 3, 10, 38, 371623),
            'raw': '-1', 'sensor_id': 77, 'name': 'TEMP', 'value': '17.40'}
        # TODO: pass it into a try catch, it doesn't catch the exception,
        #        maybe because it s raised from another package. 
        # self.assertRaises(
        #     IntegrityError, 
        #     self.station._insert_metering(metering))
        
    def test__got_meterings_raw_data(self):
        def str_received():
            return 'data received'
            
        def nothing_yet():
            return '' 
            
        self.station.ser.readline = str_received
        self.assertEqual(True, self.station._got_meterings_raw_data())
        self.station.ser.readline = nothing_yet
        self.assertEqual(False, self.station._got_meterings_raw_data())   
        
        
        
                     
