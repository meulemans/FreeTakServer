#######################################################
# 
# point.py
# Python implementation of the CoT point
# Generated by Enterprise Architect
# Created on:      11-Feb-2020 11:08:07 AM
# Original author: Corvo
# 
#######################################################


class COTPoint:


  xmlPoint ='<point lat="43.967087" lon="-66.126393" hae="29.30101602610336" ce="367.1" le="9999999.0" />"'
  # Latitude referred to the WGS 84 ellipsoid in degrees
  lat = "00.00000000" 
  lon = "00.00000000" 
      # Linear 1-sigma error or an altitude range about the point in meters
  le = "9999999.0" 
      # Longitude referred to the WGS 84 in degrees
  lon = "0.000000" 
  
  # Circular 1-sigma or decimal a circular area about the point in meters
  ce = "9999999.0"

  hae = "00.00000000"

  """
  I removed hae from getXMLPoint
  """

  def __init__(self):
    self.getXMLPoint()

    # ce getter 
  def getce(self): 
    return self.ce 

    # ce setter 
  def setce(self, ce=0):  
    self.ce=ce 

    # le getter 
  def getle(self): 
    return self.le 

    # le setter 
  def setle(self,le=0):  
    self.le=le 


    # lat getter 
  def getlat(self):
    return self.lat 

    # lat setter 
  def setlat(self,lat=0):  
    self.lat=lat 

      # lon getter 
  def getlon(self): 
    return self.lon 

    # lon setter 
  def setlon(self,lon=0):  
    self.lon=lon
  
  def gethae(self):
    return self.hae

  def sethae(self,hae=0):
    self.hae = hae

  def getXMLPoint(self):
    self.apoint = '<point lat="'+self.lat+'" lon="'+self.lon+'" ce="'+self.ce+'" le="'+self.le+'" hae="'+self.hae+'"/>"'
    return self.apoint