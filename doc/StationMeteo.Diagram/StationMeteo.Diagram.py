class Station :
	def __init__(self) :
		self.ser = SerialInput() # 
		self.parser = InputParser() # 
		self.datab = DatabManager() # 
		self.input = None # str
		self.sensor_dict = dict('id': ,'name': ) # 
		self.last_meterings_list = LastMeteringList() # 
		pass
	def __get_serial_input_content (self, ser) :
		# returns 
		pass
	def __parse (self, serial_input_content) :
		# returns 
		pass
	def __store_meterings (self) :
		# returns 
		pass
	def __connect_serial (self) :
		# returns 
		pass
	def setup (self) :
		# returns 
		pass
	def loop (self) :
		# returns 
		pass
class DatabManager :
	'''
http://docs.sqlalchemy.org/en/rel_0_8/orm/tutorial.html#adding-new-objects'''
	def __init__(self) :
		self.engine_url = 'sqlite:///:memory:' # str
		self.engine = sqlalchemy.create_engine(engine_url, echo = True) # 
		self.Session = sqlalchemy.orm.sessionmaker(bind=engine) # 
		self.session = Session() # 
		self.metering = Metering() # 
		self.Sensors = Sensors() # 
		pass
class Sensors :
	'''
https://www.google.fr/#q=NVARCHAR+encodage+mysql
https://stackoverflow.com/questions/612430/when-must-we-use-nvarchar-nchar-instead-of-varchar-char-in-sql-servers

Nvarchar ne sert que pour les utilisateurs MS-SQL. '''
	def __init__(self) :
		pass
class Metering :
	'''
http://docs.sqlalchemy.org/en/rel_0_8/orm/tutorial.html#declare-a-mapping

>>> from sqlalchemy.ext.declarative import declarative_base
>>> declarative_base()
<class 'sqlalchemy.ext.declarative.Base'>
>>> 
'''
	def __init__(self) :
		pass
class /dev/tty :
	def __init__(self) :
		self.name = None # string
		pass
class SerialInput :
	'''
>>> from serial import Serial
>>> Serial()
Serial<id=0xb767eb6c, open=False>(port=None, baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)
>>> help(Serial())
>>> help(Serial.readline())
>>> help(Serial.readlines())
'''
	def __init__(self) :
		self.port = '/dev/ttyUSB0' # 
		self.baudrate = 115200 # int
		pass
	def readline (self) :
		# returns str
		pass
class InputParser :
	def __init__(self) :
		self.serial_input_content = None # str
		self.last_meterings_list = LastMeteringList() # 
		pass
	def parse (self, ) :
		# returns 
		pass
class LastMeteringList :
	def __init__(self) :
		pass
