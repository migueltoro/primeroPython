'''
Created on Jun 21, 2019

@author: Miguel Toro
'''

def mapValues(dictionary, f):
    return {k:f(k,v) for k,v in dictionary.items()}

def list_get(ls,idx,default):
    try:
        return ls[idx]
    except IndexError:
        return default

if __name__ == '__main__':
    pass