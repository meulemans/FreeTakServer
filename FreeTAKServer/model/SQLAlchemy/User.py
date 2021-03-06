#######################################################
# 
# User.py
# Python implementation of the Class User
# Generated by Enterprise Architect
# Created on:      21-Sep-2020 10:28:08 PM
# Original author: natha
# 
#######################################################
from sqlalchemy import Column
from FreeTAKServer.model.SQLAlchemy.Root import Base
from sqlalchemy import String


class User(Base):
# default constructor  def __init__(self):  

    """sqlalchemy object of table of connected users and their information
    """
    __tablename__ = "User"
    uid = Column(String(25), primary_key = True)
    callsign = Column(String)