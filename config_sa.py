# -*- coding: utf-8 -*- line endings: unix -*-
__author__ = 'quixadhal'

from sqlalchemy import Column, Integer, Boolean, DateTime
import log_system
from db_system_sa import DataBase

logger = log_system.init_logging()


class Option(DataBase):
    __tablename__ = 'option'

    date_created = Column(DateTime, primary_key=True)
    version = Column(Integer)
    port = Column(Integer)
    wizlock = Column(Boolean, default=False)
