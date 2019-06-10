'''
Created on Jun 5, 2019

@author: Miguel Toro
'''

from math import sqrt
from us.lsi.data.coordenadas2D import Coordenadas2D

class Coordenadas3D:
    '''
    classdocs
    '''
    def __init__(self,latitude,longitude,altitude):
        '''
        Constructor
        '''
        self.latitude=latitude
        self.longitude=longitude
        self.altitude=altitude
    
    def to2D(self):
        return Coordenadas2D(self.latitude,self.longitude)
        
   
    def distance(self,other): 
        c1 = self.to2D()
        c2 = other.to2D()
        d_2d = c1.distance(c2)
        inc_alt = self.altitude-other.altitude
        return sqrt(inc_alt**2 + d_2d**2)
        
    def __str__(self):
        return '({0:>20},{1:>20},{2:>20})'.format(self.latitude,self.longitude,self.altitude)