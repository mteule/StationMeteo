import unittest

from station_meteo.station import Station

class MyTest(unittest.TestCase):
    def setUp(self):
        self.session = 'foobar'
        self.station = Station()
        self.station.raw_received_meterings = (
            "TEMP,-1,17.40,HUM,-1,57.50,NO2,4236,15.4445400238,CO,125283," +
            "17411.0546875000,VOC,141338,22.7283306121,Dust,2776,0.0003270847" +
            "\n\r")

        
    def tearDown(self):
        self.session = None
        self.station  # TODO: know if a close() function is necessary

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

    def test__refresh_sensor_id_dict(self):
        a = {'CO': 3, 'TEMP': 1, 'VOC': 5, 'Dust': 6, 'HUM': 2, 'NO2': 4}
        self.station._refresh_sensor_id_dict()
        self.assertEqual(a, self.station.sensor_id_dict)
        
        
