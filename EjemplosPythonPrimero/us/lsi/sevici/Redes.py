'''
Created on Jun 10, 2019

@author: Miguel Toro
'''

import requests
import json
from us.lsi.sevici.Red import Red
from us.lsi.tools.FIterable import FIterable

url = "http://api.citybik.es/v2/networks"

class Redes:
    '''
    classdocs
    '''    
    
    @staticmethod 
    def ofUrl():
        response = requests.get(url)
        data = json.loads(response.text)
        redes = [Red.ofData(x) for x in data['networks']]
        return Redes(redes)
    
        

    def __init__(self, redes):
        '''
        Constructor
        '''
        self.redes = redes   
    
    
    def existRedCityInCountry(self, country, city):
        return any(r.country == country and r.city == city for r in self.redes)    
    
    def citiesWhithSeveralNetworks(self):
        groups = FIterable(self.redes).counting(lambda r: r.city)
        return [r.city for r in self.redes if groups[r.city]>1]
    
    def allByCountry(self,country):
        return [r for r in self.redes if r.country == country]    
    
    def allByCountryAndCity(self,country,city):
        return [r for r in self.redes if r.country == country and r.city == city]
    
    def byCountryAndCityAndName(self, country,city,name):
        return [r for r in self.allByCountryAndCity(country,city) if r.name == name]
    
    def countries(self):
        return [r.country for r in self.redes]

    def cities(self, country):
        return [r.city for r in self.redes if r.country == country]
        
    def __str__(self):
        return '\n'.join(str(e) for e in self.redes)
        