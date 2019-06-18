'''
Created on Jun 15, 2019

@author: Miguel Toro
'''

import numpy
    
'''
* @param limitExcluded Un entero
* @return Un entero aleatorio en el intervalo 0..limitExcluded con el extremo derecho excluido
'''
def intRandom(limitExcluded):   
    return numpy.random.randint(0,limitExcluded)


if __name__ == '__main__':
    pass