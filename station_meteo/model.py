#autogenerated by sqlautocode

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation


DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata

class Metering(DeclarativeBase):
    __tablename__ = 'Metering'

    __table_args__ = {}

    #column definitions
    date = Column(u'date', DATE())
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False)
    sensor_id = Column(u'sensor_id', INTEGER(), ForeignKey('Sensor.id'))
    value = Column(u'value', FLOAT())

    #relation definitions
    Sensor = relation('Sensor', primaryjoin='Metering.sensor_id==Sensor.id')


class Sensor(DeclarativeBase):
    __tablename__ = 'Sensor'

    __table_args__ = {}

    #column definitions
    bus_adress = Column(u'bus_adress', VARCHAR(length=255))
    description = Column(u'description', VARCHAR(length=255))
    high_threshold = Column(u'high_threshold', FLOAT())
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False)
    low_threshold = Column(u'low_threshold', FLOAT())
    max_value = Column(u'max_value', FLOAT())
    min_value = Column(u'min_value', FLOAT())
    name = Column(u'name', VARCHAR(length=255))
    unique_key = Column(u'unique_key', VARCHAR(length=255))
    unit = Column(u'unit', VARCHAR(length=255))
    unit_label = Column(u'unit_label', VARCHAR(length=255))

    #relation definitions


