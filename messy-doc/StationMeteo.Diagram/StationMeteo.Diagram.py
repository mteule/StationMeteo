class Sensor :
	'''
https://www.google.fr/#q=NVARCHAR+encodage+mysql
https://stackoverflow.com/questions/612430/when-must-we-use-nvarchar-nchar-instead-of-varchar-char-in-sql-servers

Nvarchar ne sert que pour les utilisateurs MS-SQL. '''
	def __init__(self) :
		pass
class Station :
	'''(NULL)'''
	def __init__(self) :
		self.logger = logging.getLogger(__name__) # 
		self.ser = serial.Serial() # 
		self.datab = DatabManager() # 
		self.raw_received_meterings = "" # str
		self.metering_quantity = 0 # int
		self.last_meterings_list = list() # 
		self.sensor_dict = dict('id': ,'name': ) # 
		pass
	def _get_meterings_raw_data (self) :
		# returns 
		pass
	def _parse_raw_data (self) :
		# returns 
		pass
	def _store_meterings (self) :
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
		self.logger = logging.getLogger(__name__) # 
		self.engine_url = 'sqlite:///:memory:' # str
		self.engine = sqlalchemy.create_engine(engine_url, echo = True) # 
		self.Session = sqlalchemy.orm.sessionmaker(bind=engine) # 
		self.session = Session() # 
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
