'''
Created on Jun 4, 2019

@author: Miguel Toro
'''

from math import sin, cos, sqrt, atan2, radians

class Coordenadas2D:
    '''
    classdocs
    '''
    def __init__(self,latitude,longitude):
        '''
        Constructor
        '''
        self.latitude=latitude
        self.longitude=longitude
      
    
    def distance(self, other):  
        radio_tierra = 6373.0
        latitud_a, longitud_a = radians(self.latitude), radians(self.longitude)
        latitud_b, longitud_b = radians(other.latitude), radians(other.longitude)    
        inc_lat  = latitud_b - latitud_a
        inc_long = longitud_b - longitud_a

        a = sin(inc_lat / 2)**2 + cos(latitud_a) * cos(latitud_b) * sin(inc_long / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return radio_tierra * c
    
    def esCercana(self, c, d):
        return self.distance(c) <=d;
    
    def __str__(self):
        return '({0},{1})'.format(self.latitude,self.longitude)
       
