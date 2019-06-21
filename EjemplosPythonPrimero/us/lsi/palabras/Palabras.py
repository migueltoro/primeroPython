'''
Created on Jun 5, 2019

@author: Miguel Toro
'''


from us.lsi.tools import FileTools
import re
import collections
from us.lsi.tools.FIterable import FIterable

def palabras(file):
    lineas = FileTools.lineas(file,encoding='utf-16')
    palabras = (p for linea in lineas for p in re.split(r'[ ,;.\n():\"]' ,linea) if len(p) >0) 
    return palabras

def palabrasDistintas(file):
    return FIterable(palabras(file)).distinct()

def numeroDePalabrasDistintas(file): 
    return FIterable(palabrasDistintas(file)).size()

def frecuenciasDePalabras(file):
    return collections.Counter(palabras(file))

def gruposDePalabrasPorFrecuencias(file):
    counter = frecuenciasDePalabras(file)
    return FIterable(counter.items()).grouping(lambda x: x[1],fmap = lambda x: x[0])

def gruposDeLineas(file):
    lineas = FileTools.lineas(file,encoding='utf-16')
    palabras = ((i,p) for i,linea in enumerate(lineas) for p in re.split(r'[ ,;.\n():\"]',linea) if len(p) >0) 
    return FIterable(palabras).grouping(lambda x: x[1],fmap = lambda x: x[0])

if __name__ == '__main__':
    pass