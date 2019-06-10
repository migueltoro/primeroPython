'''
Created on Jun 5, 2019

@author: Miguel Toro
'''

from us.lsi.tools import FileTools
import re
import collections
from us.lsi.tools import Collectors

def palabras(file):
    lineas = FileTools.lineas(file,encoding='utf-16')
    palabras = (p for linea in lineas for p in re.split(r'[ ,;.\n():\"]',linea) if len(p) >0) 
    return palabras

def palabrasDistintas(file):
    return Collectors.unique_values(palabras(file))

def numeroDePalabrasDistintas(file): 
    return Collectors.count(palabrasDistintas(file))

def frecuenciasDePalabras(file):
    return collections.Counter(palabras(file))

def gruposDePalabrasPorFrecuencias(file):
    counter = frecuenciasDePalabras(file)
    return Collectors.grouping(counter.items(),lambda x: x[1],fmap = lambda x: x[0])

def gruposDeLineas(file):
    lineas = FileTools.lineas(file,encoding='utf-16')
    palabras = ((i,p) for i,linea in enumerate(lineas) for p in re.split(r'[ ,;.\n():\"]',linea) if len(p) >0) 
    return Collectors.grouping(palabras,lambda x: x[1],fmap = lambda x: x[0])

if __name__ == '__main__':
    pass