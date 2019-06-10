'''
Created on Jun 4, 2019

@author: Miguel Toro
'''

import csv
from us.lsi.ruta.Marca import Marca
from us.lsi.tools import Graphics

class Ruta:
    '''
    classdocs
    '''
    
    def __init__(self, marcas):
        '''
        Constructor
        '''
        self.marcas = marcas
        
    @staticmethod   
    def ofFile(file):
        with open(file, encoding='utf-8') as f:
            lector = csv.reader(f)
            puntos =[Marca.parse(linea) for linea in lector]
            return Ruta(puntos)
        
    
    def longitud(self,i=None):
        if(i):
            return self.marcas[i].distance(self.marcas[i+1])
        else:
            return sum((self.marcas[i].distance(self.marcas[i+1]) for i in range(len(self.marcas)-1)))
    
    def duracion(self,i=None):
        if(i):
            return (self.marcas[i+1].tiempo - self.marcas[i].tiempo).seconds/3600
        else: 
            return (self.marcas[len(self.marcas)-1].tiempo - self.marcas[0].tiempo).seconds/3600
    
    def velocidad(self,i=None):
        if(i):
            return self.longitud()/self.duracion() 
        else: 
            return [(i,self.longitud(i)/self.duracion(i)) for i in range(len(self.marcas)-1) if self.duracion(i)!=0] 
     
    def mostrarAltitud(self,fileOut):
        alturas = [str(self.marcas[i].coordenadas.altitude) for i in range(len(self.marcas))]
        indices = [i for i in range(len(self.marcas))]
        campos = ["Posicion","Altura"]
        Graphics.lineChart(fileOut,"Ruta Ronda",campos,[indices,alturas])
           
    def __str__(self):
        return '\n'.join(str(x) for x in self.marcas)