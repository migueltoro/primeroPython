'''
Created on Jun 21, 2019

@author: Miguel Toro
'''

def mapValues(dictionary, f):
    return {k:f(k,v) for k,v in dictionary.items()}


if __name__ == '__main__':
    pass