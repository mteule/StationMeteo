import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)



raw_received_meterings = ("TEMP,-1,17.40,HUM,-1,57.50,NO2,4236,15.4445400238,CO,125283," +
    "17411.0546875000,VOC,141338,22.7283306121,Dust,2776,0.0003270847\n\r")
raw_received_meterings
help(raw_received_meterings)

data # ?
data = raw_received_meterings.rstrip() 
data 
help(data)

split # list()
split = [elem.strip() for elem in data.split(',')]
split
help(split) #list

metering_quantity = len(split) / 3
metering_quantity

# Check only the data won't get us into "pointer out of cast" troubles:
if not (0 == len(split) % metering_quantity):
	raise StandartError("raw data is not consistent")


last_meterings_list = list()
metering = dict()
metering = dict({'name': 'some_sensor_name', 'raw': 0, 'value': 0})
metering

# some help: http://www.tutorialspoint.com/python/python_dictionary.htm
for i in range (0, metering_quantity):
    metering ['name'] = split[(i*3 + 0)]
    metering ['raw'] = split[(i*3 + 1)]
    metering ['value'] = split[(i*3 + 2)]
    last_meterings_list.append(metering)
    metering #debug


last_meterings_list #debug




        split = [elem.strip() for elem in data.split(',')]
        logging.debug("split:")
        logging.debug(split)
        # check consistance
        if len(split) % 3 == 0:
            current = 0
            while(current != len(split)):
                name = split[current]
                raw = split[current+1]
                value = split[current+2]
                thresholds = self.datamanager.get_thresholds(name)
                if thresholds:
                    id = self.datamanager.get_id(name)
                    if self.debug:
                        print "ID : ", id
                        print "Name : ", name
                        print "Raw : ", raw
                        print "Value : ", value
                        print "Thresholds : ", thresholds
                    new_sensor = Sensor(id, name, raw, value, thresholds)
                    self.sensors.append(new_sensor)
                else: 
                    logging.debug("no thresholds found, don't create Sensor object for " + name)
                current += 3
            logging.debug("data is consistent")
            return True
        else:
            logging.debug("data is consistent")
            return False
            
            
            
            

    def _parse_raw_data () :
        raw_received_meterings = "" # str
        metering_quantity = 0 # int
        last_meterings_list = list() # 
        # returns 
        pass
