'''
Created on Jun 7, 2019

@author: Miguel Toro
'''

from us.lsi.data.coordenadas2D import Coordenadas2D

class Estacion:
    '''
    classdocs
    '''
    
    n = 0
    
    @staticmethod  
    def next(): 
        old = Estacion.n
        Estacion.n = Estacion.n+1
        return old

    def __init__(self, numero, name, slots, empty_slots, ubicacion):
        '''
        Constructor
        '''
        self.numero = numero
        self.name = name
        self.slots = slots
        self.empty_slots = empty_slots
        self.ubicacion = ubicacion
       
    @staticmethod   
    def parse(linea):
        nameCompuesto = linea[0]
        partes = nameCompuesto.split("_")
        numero = int(partes[0])
        name = partes[1]
        slots = int(linea[1])
        empty_slots = int(linea[2])
        ubicacion = Coordenadas2D(float(linea[4]),float(linea[5]))
        return Estacion(numero,name, slots, empty_slots, ubicacion)
    
    @staticmethod
    def of(station): 
        numero = int(station['extra']['uid']) if(station['extra']['uid']) else Estacion.next()
        name = station['name'] 
        empty_slots = int(station['empty_slots']) if(station['empty_slots']) else 0
        slots = int(station['free_bikes'])+empty_slots if(station['free_bikes']) else 0
        ubicacion = Coordenadas2D(float(station['latitude']), float(station['longitude']))
        return Estacion(numero,name, slots,empty_slots,ubicacion)
    
    def free_bikes(self):
        return self.slots-self.empty_slots
        
    def __str__(self):
        return '{0:35s}  {1:2d}  {2:2d}  {3:2d}  {4:s}'.format(self.name,self.slots,self.empty_slots,self.free_bikes(),str(self.ubicacion));