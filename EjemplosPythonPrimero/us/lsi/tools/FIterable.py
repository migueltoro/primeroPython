'''
Created on Jun 13, 2019

@author: Miguel Toro
'''

from us.lsi.tools import Collectors
from us.lsi.tools import FileTools
from functools import reduce

class FIterable:
    '''
    classdocs
    '''
    
    def __init__(self, iterable):
        '''
        Constructor
        '''
        self.iterable = iterable
    
    @staticmethod
    def lineas(file,encoding='utf-8'):
        return FIterable(FileTools.lineas(file,encoding=encoding))
    
    @staticmethod
    def lineasCSV(file,delimiter = ","):
        return FIterable(FileTools.lineasCSV(file,delimiter=delimiter))
       
    @staticmethod
    def iterate(initial, predicate, operator):
        return FIterable(Collectors.iterate(initial, predicate, operator))
             
    @staticmethod 
    def range(start, stop, step=1):
        return FIterable(range(start, stop, step))
    
    @staticmethod
    def concat(*iterables):
        return FIterable(Collectors.concat(iterables))
    
    @staticmethod
    def random(n,a,b):
        return FIterable(Collectors.random_iterable(n, a, b))
          
    def filter(self,predicate):
        return FIterable((x for x in self.iterable if(predicate(x))))
    
    def map(self,f):
        return FIterable((f(x) for x in self.iterable))
    
    def distinct(self):
        return FIterable(Collectors.unique_values(self.iterable))
    
    def limit(self,n):
        return FIterable(Collectors.limit(self.iterable,n))
    
    def flat(self):
        return FIterable(Collectors.flat(self.iterable))
    
    def sort(self, key = None, reverse = False):
        return FIterable(sorted(self.iterable,key=key,reverse= reverse))
    
    def grouping(self,f,fmap=None,fred=None,initial=None):
        return Collectors.grouping(self.iterable, f, fmap=fmap, fred=fred, initial=initial)
    
    def any(self,predicate):
        return any(predicate(x) for x in self.iterable)
    
    def all(self,predicate):
        return all(predicate(x) for x in self.iterable)
    
    def counting(self,f):
        return Collectors.counting(self.iterable,f)
    
    def count(self):
        return Collectors.count(self.iterable)
    
    def min(self,f):
        return min(self.iterable)
    
    def max(self,f):
        return max(self.iterable)
    
    def sum(self):
        return sum(self.iterable)
    
    def average(self):
        return sum(self.iterable)/float(self.count())
    
    def reduce(self,op):
        return reduce(op,self.iterable)    
    
    def groupingSet(self,f):
        return Collectors.groupingSet(self.iterable, f)
    
    def toList(self):
        return [x for x in self.iterable]
    
    def toSet(self):
        return {x for x in self.iterable}
        
    def __str__(self):  
        return Collectors.toStringIterable(self.iterable)