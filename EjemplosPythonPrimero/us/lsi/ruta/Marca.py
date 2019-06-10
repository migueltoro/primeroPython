'''
Created on Jun 4, 2019

@author: Miguel Toro
'''
from us.lsi.data.coordenadas3D import Coordenadas3D
from datetime import datetime


class Marca:
    '''
    classdocs
    '''

    def __init__(self, tiempo, latitud, longitud, altitud):
        '''
        Constructor
        '''
        self.tiempo = tiempo
        self.coordenadas = Coordenadas3D(latitud, longitud, altitud)
    
    @staticmethod   
    def parse(linea):
        tiempo,latitud,longitud,altitud = linea
        tiempo,latitud,longitud,altitud = datetime.strptime(tiempo,'%H:%M:%S'), float(latitud), float(longitud), float(altitud)
        return Marca(tiempo, latitud, longitud, altitud/1000)
    
    def distance(self,other):
        return self.coordenadas.distance(other.coordenadas)
    
    def __str__(self):
        return '({0},{1})'.format(self.tiempo.strftime("%H:%M:%S"),self.coordenadas) 