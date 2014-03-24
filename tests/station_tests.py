import unittest

from station_meteo.station import Station
# TODO: change the sqlalchemy.Engine.bind imported from the model.py file

class FakeSerial(object):

    def __init__(self):
        pass
    pass


class MyTest(unittest.TestCase):  # TODO: Find a name!
    """"""
    def setUp(self):
        self.session = 'foobar'
        self.station = Station()
        self.station.last_meterings.raw_string = (
            "TEMP,-1,17.40,HUM,-1,57.50,NO2,4236,15.4445400238,CO,125283," +
            "17411.0546875000,VOC,141338,22.7283306121,Dust,2776,0.0003270847" +
            "\n\r")
        pass

    def tearDown(self):
        self.session = None
        del self.station  # TODO: know if a close() function is necessary
        pass






