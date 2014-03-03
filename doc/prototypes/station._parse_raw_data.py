import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)



# Interactive script:###########################################################

raw_received_meterings = ("TEMP,-1,17.40,HUM,-1,57.50,NO2,4236,15.4445400238,CO,125283," +
    "17411.0546875000,VOC,141338,22.7283306121,Dust,2776,0.0003270847\n\r")

# http://docs.python.org/2/library/stdtypes.html#str.rstrip
data = raw_received_meterings.rstrip() 
data 
type(data)

# http://docs.python.org/2/library/stdtypes.html#str.strip
split = [elem.strip() for elem in data.split(',')]
split
type(split) #list

metering_quantity = len(split) / 3
metering_quantity

# Check only the data won't get us into "pointer out of cast" troubles:
if not (0 == len(split) % metering_quantity):
	raise StandartError("raw data is not consistent")

metering = dict({'name': 'some_sensor_name', 'raw': 0, 'value': 0})
metering

last_meterings_list = list()


# some help: http://www.tutorialspoint.com/python/python_dictionary.htm
for i in range (0, metering_quantity):
    metering ['name'] = split[(i*3 + 0)]
    metering ['raw'] = split[(i*3 + 1)]
    metering ['value'] = split[(i*3 + 2)]
    last_meterings_list.append(metering)
    metering #debug


last_meterings_list #debug


# To a function: ############################################################### 
            
def _parse_raw_data (raw_received_meterings=""):
    data = raw_received_meterings.rstrip() 
    split = [elem.strip() for elem in data.split(',')]
    metering_quantity = len(split) / 3
    # Check only the data won't get us into "pointer out of cast" troubles:
    if not (0 == len(split) % metering_quantity):
    	raise StandartError("raw data is not consistent")
    	
    metering = dict({'name': 'some_sensor_name', 'raw': 0, 'value': 0})
    last_meterings_list = list()
    for i in range (0, metering_quantity):
        metering ['name'] = split[(i*3 + 0)]
        metering ['raw'] = split[(i*3 + 1)]
        metering ['value'] = split[(i*3 + 2)]
        last_meterings_list.append(metering)
    return last_meterings_list



result = _parse_raw_data (raw_received_meterings)
result
