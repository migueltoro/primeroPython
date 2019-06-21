'''
Created on Jun 5, 2019

@author: Miguel Toro
'''

import re

def transform(inText,reglas):
    outText = inText;
    for e,s in reglas.items():
        outText = re.sub(r'\{'+e+'\}',s,outText)
    return outText;

def to_unicode(r):
    return str(r).encode('cp850', errors='replace').decode('cp850')
    

if __name__ == '__main__':
    pass