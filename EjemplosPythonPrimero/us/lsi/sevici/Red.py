'''
Created on Jun 7, 2019

@author: Miguel Toro
'''

from us.lsi.data.coordenadas2D import Coordenadas2D
from us.lsi.sevici.Estacion import Estacion
from us.lsi.tools import FileTools
import requests
import json
from us.lsi.tools.Collectors import list_get 

url = 'http://api.citybik.es'
file = '../../../resources/estaciones.csv'

class Red:
    '''
    classdocs
    '''
    
    @staticmethod 
    def ofFile():
        name = 'Sevici'
        href = None
        country = 'ES'
        city = 'Sevilla'
        ubicacion = Coordenadas2D(37.388096,-5.982330);
        r = Red(name, href, country, city, ubicacion)
        lineas = FileTools.lineasCSV(file)[1:]
        r.estaciones = [Estacion.parse(e) for e in lineas]
        return r
    
    
    
    @staticmethod 
    def ofData(network):
        name = network['name'] 
        href = network['href']
        country = network['location']['country']
        city = network['location']['city']
        ubicacion = Coordenadas2D(float(network['location']['latitude']),float(network['location']['longitude']))
        return Red(name, href, country, city, ubicacion)
    
    @staticmethod 
    def of(suffix):
        response = requests.get(url+suffix)
        data = json.loads(response.text)
        network = data['network']
        name = network['name'] 
        href = network['href']
        country = network['location']['country']
        city = network['location']['city']
        ubicacion = Coordenadas2D(float(network['location']['latitude']),float(network['location']['longitude']))
        r = Red(name, href, country, city, ubicacion)
        r.estaciones = [Estacion.of(station) for station in network['stations']]
        return r

    def byNumero(self, numero):
        return list_get([e for e in self.estaciones if(e.numero == numero)],0,'No existe ese numero')
    
    def cercanas(self, coordenadas, distance):
        return [e for e in self.estaciones if(e.ubicacion.esCercana(coordenadas,distance))]
    
    def __init__(self, name, href, country, city, ubicacion):
        '''
        Constructor
        '''
        self.name = name
        self.href = href
        self.country = country
        self.city = city
        self.ubicacion = ubicacion
        self.estaciones = None
        
    def __str__(self):
        if(self.estaciones):
            return 'Nombre = {0:s}\nEstaciones\n{1:s}'.format(self.name,'\n'.join(str(e) for e in self.estaciones))
        else :
            return '({0},{1},{2})'.format(self.name,self.country,self.city)