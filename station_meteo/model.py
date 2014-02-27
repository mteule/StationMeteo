# coding: utf-8
from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Metering(Base):
    __tablename__ = u'Metering'

    id = Column(Integer, primary_key=True)
    value = Column(Float)
    datetime = Column(DateTime)
    sensor_id = Column(Integer)
    raw = Column(Integer)


class Sensor(Base):
    __tablename__ = u'Sensor'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    high_threshold = Column(Float)
    low_threshold = Column(Float)
    min_value = Column(Float)
    max_value = Column(Float)
    unit = Column(String(255))
    unit_label = Column(String(255))
    unique_key = Column(String(255))
    bus_adress = Column(String(255))
