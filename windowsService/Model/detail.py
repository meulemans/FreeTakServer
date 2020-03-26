#######################################################
#
# detail.py
# Python implementation of the Class detail
# Generated by Enterprise Architect
# Created on: 11-Feb-2020 11:08:07 AM
# Original author: Corvo
#
#######################################################
from status import status
from color import color
from link import link
from contact import contact
from usericon import usericon
from remarks import remarks
from takv import takv
from track import track
from Precisionlocation import Precisionlocation
from __chat import __chat as m___chat
from __serverdestination import __serverdestination as m___serverdestination

class detail:
    """An optional element used to hold CoT sub-schema. empty element
    """
    # default constructor def __init__(self):
    m_Precisionlocation= Precisionlocation()

    m_status = "status()" 
     # m_status getter 
    def getm_status(self): 
        return self.m_status 
 
     # m_status setter 
    def setm_status(self,m_status=0):  
        self.m_status = m_status 
 
    m_color = "color()" 
     # m_color getter 
    def getm_color(self): 
        return self.m_color 
 
     # m_color setter 
    def setm_color(self,m_color=0):  
        self.m_color = m_color 
 
    m_link = "link()" 
     # m_link getter 
    def getm_link(self): 
        return self.m_link 
 
     # m_link setter 
    def setm_link(self,m_link=0):  
        self.m_link = m_link 
 
    m_contact = "contact()" 
     # m_contact getter 
    def getm_contact(self): 
        return self.m_contact 
 
     # m_contact setter 
    def setm_contact(self,m_contact=0):  
        self.m_contact = m_contact 
 
    m_usericon = "usericon()" 
     # m_usericon getter 
    def getm_usericon(self): 
        return self.m_usericon 
 
     # m_usericon setter 
    def setm_usericon(self,m_usericon=0):  
        self.m_usericon = m_usericon 
 
    m_remarks = "remarks()" 
     # m_remarks getter 
    def getm_remarks(self): 
        return self.m_remarks 
 
        # m_remarks setter 
    def setm_remarks(self,m_remarks=0):  
        self.m_remarks = m_remarks 
 
    m_takv = "takv()" 
        # m_takv getter 
    def getm_takv(self): 
        return self.m_takv 
 
        # m_takv setter 
    def setm_takv(self,m_takv=0):  
        self.m_takv = m_takv 
 
    m_track = "track()" 
        # m_track getter 
    def getm_track(self): 
        return self.m_track 
 
        # m_track setter 
    def setm_track(self,m_track=0):  
        self.m_track = m_track 
