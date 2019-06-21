'''
Created on Jun 13, 2019

@author: Miguel Toro
'''
from collections import Iterable
from us.lsi.tools import FileTools
from functools import reduce
import math
from random import randint


def concat(*iterables):
    for it in iterables:
        if isinstance(it,Iterable):
            for e in it:
                yield e 
        else:
            yield it


def unique_values(iterable):
    seen = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item 

def iterate(initial, predicate, operator):
    e = initial
    while predicate(e):
        yield e
        e = operator(e)
        

class FIterable:
    '''
    classdocs
    '''
    
    def __init__(self, iterable):
        '''
        Constructor
        '''
        self.iterable = iterable
        
    def __iter__(self):
        return iter(self.iterable)
    
    @staticmethod
    def lineas(file,encoding='utf-8'):       
        return FIterable(FileTools.lineas(file,encoding=encoding))
    
    @staticmethod
    def seqLineas(file,encoding='utf-8'):
        with open(file, "r", encoding=encoding) as f:
            return FIterable(f)
    
    @staticmethod
    def lineasCSV(file,delimiter = ","):
        return FIterable(FileTools.lineasCSV(file,delimiter=delimiter))  
       
    @staticmethod
    def iterate(initial, predicate, operator):
        return FIterable(iterate(initial, predicate, operator))
             
    @staticmethod 
    def range(start, stop, step=1):
        return FIterable(range(start, stop, step))
    
    @staticmethod
    def concat(*iterables):
        return FIterable(concat(iterables))
    
    @staticmethod
    def random(n,a,b):
        return FIterable(randint(a,b) for _ in range(n))
          
    def filter(self,predicate):
        return FIterable(x for x in self.iterable if(predicate(x)))
    
    def map(self,f):
        return FIterable(f(x) for x in self.iterable)
    
    def distinct(self):
        return FIterable(unique_values(self.iterable))
    
    def limit(self,n):
        s = zip(self.iterable,range(n))
        return FIterable(x for x,_ in s)
    
    def flatMap(self,f):
        return FIterable(y for x in self.iterable for y in f(x))
    
    def sort(self, key = None, reverse = False):
        return FIterable(sorted(self.iterable,key=key,reverse= reverse))
    
    def grouping(self,f,fmap=None,fred=None,initial=None):
        r = {}
        for x in self.iterable:
            k = f(x)
            if(k in r.keys()):
                r[k].append(x)
            else:
                r[k] = [x]
        if fmap:
            s = {k:[fmap(x) for x in v] for k,v in r.items()}
        else:
            s = r
        if fred and initial:
            q = {k:reduce(fred,v,initial) for k,v in s.items()}
        elif fred:
            q = {k:reduce(fred,v) for k,v in s.items()}
        else:
            q = s
        return q 
    
    def partitioning(self,predicate):
        return self.grouping(predicate)
    
    def joining(self,separator='\n',prefix='',suffix=''):
        return '{0}{1}{2}'.format(prefix,separator.join(str(x) for x in  self.iterable),suffix)
    
    def any(self,predicate):
        return any(predicate(x) for x in self.iterable)
    
    def all(self,predicate):
        return all(predicate(x) for x in self.iterable)
    
    def counting(self,f):
        r = {}
        for x in self.iterable:
            k = f(x)
            if(k in r.keys()):
                r[k] = r[k]+1
            else:
                r[k] = 1
        return r
    
    def size(self):
        n = 0
        for _ in self.iterable:
            n = n+1
        return n
    
    def min(self,f):
        return min(self.iterable)
    
    def max(self,f):
        return max(self.iterable)
    
    def sum(self):
        return sum(self.iterable)
    
    def average(self):
        s = 0
        n = 0
        for x in self.iterable:
            s = s + x 
            n = n+1
        return s/n
    
    def index(self,predicate,default=None):
        for i,el in enumerate(self.iterable):
            if predicate(el):
                return i
        return default
        
    def reduce(self,op,initial=None):
        if not initial:
            value = next(self.iterable)
        else:
            value = initial
        for e in self.iterable:
            value = op(value, e)
        return value 
    
    def groupingSet(self,f):
        r = {}
        for x in self.iterable:
            k = f(x)
            if(k in r.keys()):
                r[k].add(x)
            else:
                r[k] = {x}
        return r  
    
    def toList(self):
        return [x for x in self.iterable]
    
    def toSet(self):
        return {x for x in self.iterable}
    
    
    def estadisticos(self):
        num = 0
        sm = 0
        sum_cuadrados = 0
        mx = None
        mn = None
        for x in self.iterable:
            num = num+1
            sm = sm+x
            sum_cuadrados = sum_cuadrados+x*x
            mx = max(mx,x) if(mx) else x
            mn = min(mn,x) if(mn) else x
        return Estadisticos(num,sm,sum_cuadrados,mx,mn)   
        
    def __str__(self):  
        return '\n'.join(str(x) for x in self.iterable)
    

class Estadisticos:   
    '''
    classdocs
    '''
    
    def __init__(self,num,sm,sum_cuadrados,mx,mn):
        '''
        Constructor
        '''
        self.num = num
        self.sum = sm
        self.sum_cuadrados = sum_cuadrados
        self.max = mx
        self.min = mn
        
    def media(self):
        return self.sum/self.num
    
    def varianza(self):        
        return self.sum_cuadrados/self.num - (self.media())**2
    
    def desviacion_tipica(self):
        return math.sqrt(self.varianza())
    
    
    def __str__(self): 
        return '{0},{1}'.format(self.num,self.sum)
    