#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>

import logging
import sqlalchemy

class DatabManager :
    '''
http://docs.sqlalchemy.org/en/rel_0_8/orm/tutorial.html#adding-new-objects'''
    def __init__(self) :
        self.logger = logging.getLogger(__name__) # 
        self.engine_url = 'sqlite:///:memory:' # str
        self.engine = sqlalchemy.create_engine(self.engine_url, echo = True) # 
        self.Session = sqlalchemy.orm.sessionmaker(bind=self.engine) # 
        self.session = self.Session() # 
        pass
