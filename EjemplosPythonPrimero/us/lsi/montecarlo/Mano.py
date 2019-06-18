'''
Created on Jun 15, 2019

@author: Miguel Toro
'''

from us.lsi.montecarlo.Card import Card
from us.lsi.tools import Math
from us.lsi.tools.FIterable import FIterable
from us.lsi.tools import Graphics

class Mano:
    '''
    classdocs
    '''

    def __init__(self, cartas):
        '''
        Constructor
        '''
        self.__cartas = cartas
        self.__frecuenciasDeValores = None
        self.__valoresOrdenadosPorFrecuencias = None
        self.__son5ValoresConsecutivos = None
        self.__frecuenciasDePalos=None
        self.__palosOrdenadosPorFrecuencias= None
        self.__jugada = None
        self.__fuerza = None
      
        
    numeroDeCartas = 5   
    
    
    @staticmethod
    def of(cartas):
        return Mano(cartas)
    
    @staticmethod
    def ofText(txt): 
        txt = txt[1:len(txt)-1]
        partes = txt.split(",")        
        cartas = [Card.ofText(x) for x in partes]
        return Mano.of(cartas)
    
    @staticmethod
    def random():
        cartas = []
        for _ in range(Mano.numeroDeCartas):
            n = Math.intRandom(52)
            card = Card.ofId(n)
            cartas.append(card)
        return Mano(cartas)

    def getSon5ValoresConsecutivos(self):
        if not self.__son5ValoresConsecutivos:  
            ls = FIterable(self.getValoresOrdenadosPorFrecuencias()).sort().toList()
            if len(ls) == 5:               
                self.__son5ValoresConsecutivos = FIterable.range(0,len(ls)-1).all(lambda x: ls[x+1]-ls[x]==1)
        return self.__son5ValoresConsecutivos
    
    def getFrecuenciasDeValores(self):
        if not self.__frecuenciasDeValores:
            self.__frecuenciasDeValores = FIterable(self.__cartas).counting(lambda c:c.valor)           
        return self.__frecuenciasDeValores
    
    
    def getValoresOrdenadosPorFrecuencias(self):
        if not self.__valoresOrdenadosPorFrecuencias:
            self.__valoresOrdenadosPorFrecuencias = FIterable(self.getFrecuenciasDeValores().items()) \
                .sort(lambda e: e[1], reverse= True) \
                .map(lambda e:e[0]) \
                .toList() 
        return self.__valoresOrdenadosPorFrecuencias

    def getFrecuenciasDePalos(self):
        if not self.__frecuenciasDePalos:
            self.__frecuenciasDePalos = FIterable(self.__cartas).counting(lambda c: c.palo)
        return self.__frecuenciasDePalos

    def getPalosOrdenadosPorFrecuencias(self):
        if not self.__palosOrdenadosPorFrecuencias:
            self.__palosOrdenadosPorFrecuencias = FIterable(self.getFrecuenciasDePalos().items()) \
                .sort(lambda e: e[1],reverse = True) \
                .map(lambda e:e[0]) \
                .toList()    
        return self.__palosOrdenadosPorFrecuencias
    
    def esColor(self):
        pal0 = self.getPalosOrdenadosPorFrecuencias()[0]
        return self.getFrecuenciasDePalos()[pal0] == 5
    
    def esEscalera(self):
        return self.getSon5ValoresConsecutivos()
    
    def esPoker(self):
        val0 = self.getValoresOrdenadosPorFrecuencias()[0]
        return self.getFrecuenciasDeValores()[val0] == 4
    
    def esEscaleraDeColor(self):
        pal0 = self.getPalosOrdenadosPorFrecuencias()[0]
        return self.getSon5ValoresConsecutivos() and self.getFrecuenciasDePalos()[pal0] == 5
    
    def esFull(self):
        val0 = self.getValoresOrdenadosPorFrecuencias()[0]
        val1 = self.getValoresOrdenadosPorFrecuencias()[1]
        return self.getFrecuenciasDeValores()[val0] == 3 and \
            self.getFrecuenciasDeValores()[val1] == 2
            
    def esTrio(self):
        val0 = self.getValoresOrdenadosPorFrecuencias()[0]
        return self.getFrecuenciasDeValores()[val0] == 3
    
    def esDoblePareja(self):
        val0 = self.getValoresOrdenadosPorFrecuencias()[0]
        val1 = self.getValoresOrdenadosPorFrecuencias()[1]
        return self.getFrecuenciasDeValores()[val0] == 2 and \
            self.getFrecuenciasDeValores()[val1] == 2
    
    def esPareja(self):
        val0 = self.getValoresOrdenadosPorFrecuencias()[0]
        return self.getFrecuenciasDeValores()[val0] == 2

    def esEscaleraReal(self):
        return self.esEscaleraDeColor() and \
                FIterable(self.__cartas).map(lambda x:x.valor).toSet().contains(12)
                
    def esCartaMasAlta(self):
        return True
    
    nombres_jugadas =  ['EscaleraReal','EscaleraDeColor','Poker','Full','Color', \
                        'Escalera','Trio', \
                        'DoblePareja','Pareja','CartaMasAlta']
    
    predicados_jugadas =  [esEscaleraReal,esEscaleraDeColor,esPoker,esFull,esColor,esEscalera,esTrio, \
        esDoblePareja,esPareja,esCartaMasAlta]
                        
    def getJugada(self):
        if not self.__jugada:
            self.__jugada = FIterable(Mano.predicados_jugadas) \
                .index(lambda p: p(self)) 
        return self.__jugada
    
    def getNombreDeJugada(self):
        return Mano.nombres_jugadas[self.getJugada()]
    
    def getFuerza(self, n=1000):
        if self.__fuerza: return self.__fuerza
        gana = 0;
        pierde = 0;
        empata = 0;
        for _ in range(n):
            mr = Mano.random()
            if self < mr :
                pierde = pierde+1
            elif self > mr:
                gana = gana +1
            elif self == mr:
                empata = empata+1
        self.__fuerza = gana/(gana+pierde+empata)
        return self.__fuerza

    def toGraphics(self, fileOut):
        fuerza = self.getFuerza(5000)
        Graphics.cartasGraphic(fileOut,self.__cartas,fuerza,self.getNombreDeJugada())

    def __lt__(self,mano):
        r = False
        if  self.getJugada() > mano.getJugada():
            return True
        if self.getJugada() == mano.getJugada() and \
            self.getValoresOrdenadosPorFrecuencias()[0] < mano.getValoresOrdenadosPorFrecuencias()[0]:
            return True
        return r
    
    def __gt__(self,mano):
        return not (self  < mano) and not (self == mano)
      
    def __eq__(self,mano):
        return self.getJugada() == mano.getJugada() and \
            self.getValoresOrdenadosPorFrecuencias()[0] == mano.getValoresOrdenadosPorFrecuencias()[0]
            
    
            
    def __str__(self):
        return '{}={}={}'.format(FIterable(self.__cartas).joining(separator=',',prefix='[',suffix=']'),
                            Mano.nombres_jugadas[self.getJugada()], self.getFuerza())


    