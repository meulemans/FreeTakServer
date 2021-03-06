#######################################################
# 
# remarks.py
# Python implementation of the Class remarks
# Generated by Enterprise Architect
# Created on:      11-Feb-2020 11:08:08 AM
# Original author: Corvo
# 
#######################################################
from .RemarksVariables import RemarksVariables as vars
import datetime as dt

class Remarks:
  """Provides a place to annotate CoT with free text information.  e.g. comments
  from other users about the current COT. Used also fro the geoChat.
  the xml body of this class is used to transport the chat message
  """
  def __init__(self):
    self.time = None
    self.source = None
    self.sourceID = None
    self.to = None

  @staticmethod
  def drop_point(TIME = vars.drop_point().TIME, SOURCE = vars.drop_point().SOURCE, SOURCEID = vars.geochat().SOURCEID, INTAG = vars.geochat().INTAG):
    remarks = Remarks()
    remarks.settime(time=TIME)
    remarks.setsource(source=SOURCE)
    remarks.setsourceID(SOURCEID)
    remarks.setINTAG(INTAG)
    return remarks

  @staticmethod
  def geochat(TIME = vars.geochat().TIME, SOURCE = vars.geochat().SOURCE, SOURCEID = vars.geochat().SOURCEID, INTAG = vars.geochat().INTAG, TO = vars.geochat().TO):
    remarks = Remarks()
    remarks.settime(time=TIME)
    remarks.setsource(source=SOURCE)
    remarks.setsourceID(SOURCEID)
    remarks.setINTAG(INTAG)
    remarks.setto(TO)
    return remarks

  # time getter
  def gettime(self):
    return self.time

  # time setter
  def settime(self, time=0):
    DATETIME_FMT = "%Y-%m-%dT%H:%M:%SZ"
    if time == None:
      timer = dt.datetime
      now = timer.utcnow()
      zulu = now.strftime(DATETIME_FMT)
      self.time = zulu
    else:
      self.time = time

  # to getter
  def getto(self):
    return self.to

  # to setter
  def setto(self, to=0):
    self.to=to

  # source getter
  def getsource(self):
    return self.source

  # source setter
  def setsource(self, source=0):
    self.source=source

  def getsourceID(self):
    return self.sourceID

  # source setter
  def setsourceID(self, sourceID=0):
    self.sourceID = sourceID
    
  def setINTAG(self, INTAG):
    self.INTAG = INTAG
    
  def getINTAG(self, INTAG):
    return self.INTAG