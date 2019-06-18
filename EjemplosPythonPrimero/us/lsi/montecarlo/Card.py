'''
Created on Jun 15, 2019

@author: Miguel Toro
'''

from us.lsi.tools import Preconditions

class Card:
    '''
    classdocs
    '''

    nombreValores = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    symbolsPalos = ['C', 'H', 'S', 'D']
    nombrePalos = ["clubs","hearts","spades","diamonds"]

    def __init__(self,palo,valor):
        '''
        Constructor
        '''
        self.palo = palo # [0,4)
        self.valor = valor # [0,14)
        self.ide = palo*4+valor # [0,54)
        
    @staticmethod
    def ofText(text):     
        p = text[len(text)-1]
        v = text[0:len(text)-1]
        palo = Card.symbolsPalos.index(p)
        valor = Card.nombreValores.index(v)      
        return Card.of(palo, valor)
    
    @staticmethod
    def ofId(ide):
        Preconditions.checkArgument(ide >= 0 and ide < 52, "No es posible %d".format(ide))
        palo = ide % 4
        valor = ide % 13
        return Card(palo,valor)

    
    @staticmethod
    def of(palo,valor):
        Preconditions.checkArgument(valor >= 0 and valor <14 and palo >=0 and palo < 52, 
                    "No es posible valor = %d, palo = %d".format(valor,palo))
        return Card(palo,valor)

    
    def __str__(self): 
        return Card.nombreValores[self.valor]+Card.symbolsPalos[self.palo]

    
    
    def getNameFile(self):
        r = None
        if(self.valor<9):
            r = "resources/images/%s_of_%s.svg" % (Card.nombreValores[self.valor],Card.nombrePalos[self.palo])
        else:
            switcher = {
            9 : "resources/images/jack_of_%s.svg" % (Card.nombrePalos[self.palo]),
            10: "resources/images/queen_of_%s.svg" % (Card.nombrePalos[self.palo]),
            11: "resources/images/king_of_%s.svg" % (Card.nombrePalos[self.palo]),
            12: "resources/images/ace_of_%s.svg" % (Card.nombrePalos[self.palo])
            }
            r = switcher.get(self.valor,None)
        return r

    