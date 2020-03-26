#######################################################
# 
# remarks.py
# Python implementation of the Class remarks
# Generated by Enterprise Architect
# Created on:      11-Feb-2020 11:08:08 AM
# Original author: Corvo
# 
#######################################################


class remarks:
  """Provides a place to annotate CoT with free text information.  e.g. comments
  from other users about the current COT. Used also fro the geoChat.
  the xml body of this class is used to transport the chat message
  """
  # default constructor       def __init__(self):  

  time = "%Y-%m-%dT%H:%M:%SZ" 
  # time getter 
  def gettime(self): 
    return self.time 

  # time setter 
  def settime(self, time=0):  
    self.time=time 

  to = "" 
  # to getter 
  def getto(self): 
    return self.to 

  # to setter 
  def setto(self, to=0):  
    self.to=to 

  source = "" 
  # source getter 
  def getsource(self): 
    return self.source 

  # source setter 
  def setsource(self, source=0):  
    self.source=source 
