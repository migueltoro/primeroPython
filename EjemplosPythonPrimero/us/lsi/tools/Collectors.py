'''
Created on Jun 6, 2019

@author: Miguel Toro
'''


from random import randint
from collections import Iterable
from functools import reduce

def list_get(ls,idx,default):
    try:
        return ls[idx]
    except IndexError:
        return default
    

def concat(*iterables):
    for it in iterables:
        if isinstance(it,Iterable):
            for e in it:
                yield e 
        else:
            yield it

def flat(iterable):
    for e in iterable:
        if isinstance(e,Iterable):
            yield from flat(e)
        else:
            yield e

def unique_values(iterable):
    seen = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item 

def random_iterable(n,a,b):
    return (randint(a,b) for i in range(n))


def iterate(initial, predicate, operator):
    e = initial
    while predicate(e):
        yield e
        e = operator(e)

def limit(iterable,n):
    s = zip(iterable,range(n))
    return (x for x,_ in s)

def count(iterable):
    n = 0
    for _ in iterable:
        n = n+1
    return n

def grouping(iterable,f,fmap=None,fred=None,initial=None):
    r = {}
    for x in iterable:
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

def groupingSet(iterable,f):
    r = {}
    for x in iterable:
        k = f(x)
        if(k in r.keys()):
            r[k].add(x)
        else:
            r[k] = {x}
    return r  

def counting(iterable,f):
    r = {}
    for x in iterable:
        k = f(x)
        if(k in r.keys()):
            r[k] = r[k]+1
        else:
            r[k] = 1
    return r 

def toStringIterable(iterable,sp='\n'):
    return sp.join(str(x) for x in iterable)
    

if __name__ == '__main__':
    pass