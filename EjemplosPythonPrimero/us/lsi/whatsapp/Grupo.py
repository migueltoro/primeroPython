'''
Created on Jun 19, 2019

@author: Miguel Toro
'''

from us.lsi.tools.FIterable import FIterable
from us.lsi.whatsapp.Mensaje import Mensaje
from us.lsi.tools import Preconditions
from us.lsi.tools import FileTools
from us.lsi.tools import Graphics
import collections
import re
from us.lsi.tools.DictionaryExtension import mapValues


PalabraUsuario = collections.namedtuple('PalabraUsuario', 'palabra usuario')

class Grupo:
    '''
    classdocs
    '''

    def __init__(self,mensajes,palabrasHuecas):
        '''
        Constructor
        '''
        self.__mensajes = mensajes
        self.__palabrasHuecas = palabrasHuecas
        self.__mensajesPorUsuario = None
        self.__mensajesPorDiaDeSemana = None
        self.__mensajesPorFecha = None
        self.__mensajesPorHora = None
        self.__frecuenciasDePalabras = None
        self.__numeroDePalabras = None
        self.__frecuenciasDePalabrasPorUsuario = None
        self.__numeroDePalabrasPorUsuario = None
        self.__frecuenciasDePalabrasPorRestoDeUsuarios = None
        self.__numeroDePalabrasPorRestoDeUsuarios = None
        
    
    @staticmethod 
    def ofFile(file):
        mensajes = FIterable(FileTools.lineas(file)) \
                .filter(lambda x: x and len(x) >0) \
                .map(lambda m: Mensaje.parse(m)) \
                .filter(lambda x: x) \
                .toList()
        palabrasHuecas = FIterable(FileTools.lineas("../../../resources/palabras_huecas.txt")) \
                .filter(lambda x: len(x) >0) \
                .toSet()
        return Grupo(mensajes,palabrasHuecas)
    
    def __str__(self):
        return FIterable(self.__mensajes).map(lambda m: str(m)).joining('\n')
          
    def getMensajes(self):
        return self.__mensajes
        
    def getMensajesPorUsuario(self):
        if not self.__mensajesPorUsuario:
            self.__mensajesPorUsuario = FIterable(self.__mensajes).grouping(lambda x: x.usuario)
        return self.__mensajesPorUsuario
    
    def getNumeroDeMensajesPorUsuario(self, usuario):
        Preconditions.checkArgument(self.getMensajesPorUsuario().containsKey(usuario), \
                "No existe el usuario %s" % (usuario))
        return len(self.getMensajesPorUsuario[usuario])

    
    def getMensajesPorDiaDeSemana(self):
        if not self.__mensajesPorDiaDeSemana:
            self.__mensajesPorDiaDeSemana = FIterable(self.__mensajes) \
                .grouping(lambda x: x.fecha.weekday())
        return self.__mensajesPorDiaDeSemana
    
    def getNumeroDeMensajesPorDiaDeSemana(self, diaSemana):
        Preconditions.checkArgument(diaSemana in self.getMensajesPorDiaDeSemana(), \
                "No existe la fecha %s" % str(diaSemana))
        return len(self.__mensajesPorDiaDeSemana[diaSemana])
    
    def drawNumeroDeMensajesPorDiaDeSemana(self,fileOut):
        nombresColumna = FIterable(self.getMensajesPorDiaDeSemana()) \
                .sort() \
                .map(lambda x:str(x)) \
                .toList()
        
        datos =  FIterable(self.getMensajesPorDiaDeSemana().items()) \
                .sort(lambda x: x[0]) \
                .map(lambda x: len(x[1])) \
                .toList()
        
        nombresDatos = ["NumeroDeMensajes"]
        
        Graphics.columnsBarChart(fileOut, "MensajesPorDiaDeSemana", nombresDatos, nombresColumna, datos)
    
    
    def getMensajesPorFecha(self):
        if not self.__mensajesPorFecha:
            self.__mensajesPorFecha = FIterable(self.__mensajes).grouping(lambda x: x.fecha)
        return self.__mensajesPorFecha;
    
    def getNumeroDeMensajesPorFecha(self,fecha):
        Preconditions.checkArgument(fecha in self.getMensajesPorFecha(), \
                "No existe la fecha %s" % (str(fecha)))
        return len(self.getMensajesPorFecha[fecha])
    
    
    def getMensajesPorHora(self):
        if not self.__mensajesPorHora: 
            self.__mensajesPorHora = FIterable(self.__mensajes).grouping(lambda x:x.hora)
        return self.__mensajesPorHora
    
    def getNumeroDeMensajesPorHora(self,hora):
        Preconditions.checkArgument(hora in self.getMensajesPorHora(), \
                "No existe la fecha %s" % (str(hora)))
        return len(self.getMensajesPorHora()[hora])
    
    def getFrecuenciasDePalabras(self):
        if not self.__frecuenciasDePalabras:
            self.__frecuenciasDePalabras = FIterable(self.__mensajes) \
                    .map(lambda x: x.texto) \
                    .flatMap(lambda x: re.split(r'[ \".,:();\u00BF\u003F\u00A1\u0021]',x)) \
                    .filter(lambda x: len(x) >0) \
                    .filter(lambda x: x not in self.__palabrasHuecas) \
                    .counting(lambda x: x)
        return self.__frecuenciasDePalabras
       
    
    def getNumeroDePalabras(self):        
        if not self.__numeroDePalabras:
            self.__numeroDePalabras = FIterable(self.getFrecuenciasDePalabras().values()).sum()
        return self.__numeroDePalabras
    
  
    
    def getFrecuenciasDePalabrasPorUsuario(self):
        if not self.__frecuenciasDePalabrasPorUsuario:
            self.__frecuenciasDePalabrasPorUsuario = FIterable(self.__mensajes) \
                    .map(lambda m: PalabraUsuario(m.texto,m.usuario)) \
                    .flatMap(lambda p: FIterable(re.split(r'[ .,:();\u00BF\u003F\u00A1\u0021\"]',p.palabra)) \
                            .filter(lambda x: len(x) >0) \
                            .filter(lambda x: x not in self.__palabrasHuecas) \
                            .map(lambda x: PalabraUsuario(x,p.usuario))) \
                    .counting(lambda x: x)
        return self.__frecuenciasDePalabrasPorUsuario
    
    
    
    def getNumeroDePalabrasPorUsuario(self):
        if not self.__numeroDePalabrasPorUsuario:
            self.__numeroDePalabrasPorUsuario = FIterable(self.getFrecuenciasDePalabrasPorUsuario().items()) \
                .grouping(lambda e: e[0].usuario,lambda e: e[1], lambda x,y: x+y)
        return self.__numeroDePalabrasPorUsuario
    
    
    def getFrecuenciasDePalabrasPorRestoDeUsuarios(self):
        if not self.__frecuenciasDePalabrasPorRestoDeUsuarios:
            m = self.getFrecuenciasDePalabrasPorUsuario()
            self.__frecuenciasDePalabrasPorRestoDeUsuarios = \
                    mapValues(m,lambda k,v: self.getFrecuenciasDePalabras()[k.palabra]-v)
        return self.__frecuenciasDePalabrasPorRestoDeUsuarios
    
    
    
    def getNumeroDePalabrasPorRestoDeUsuarios(self):
        if not self.__numeroDePalabrasPorRestoDeUsuarios:
            self.__numeroDePalabrasPorRestoDeUsuarios = \
                FIterable(self.getFrecuenciasDePalabrasPorRestoDeUsuarios().items()) \
                    .grouping(lambda e: e[0].usuario,lambda e: e[1], lambda x,y: x+y)
        return self.__numeroDePalabrasPorRestoDeUsuarios

    def getImportanciaDePalabrasDeUsuario(self,palabra,usuario):
        return (self.getFrecuenciasDePalabrasPorUsuario()[PalabraUsuario(palabra, usuario)] \
                /self.getNumeroDePalabrasPorUsuario()[usuario]) * \
                (self.getNumeroDePalabrasPorRestoDeUsuarios()[usuario] \
                /self.getFrecuenciasDePalabrasPorRestoDeUsuarios()[PalabraUsuario(palabra, usuario)])
                
                
    def getPalabrasCaracteristicasDeUsuario(self,usuario,umbral):
        return FIterable(self.getFrecuenciasDePalabrasPorUsuario().items()) \
                .filter(lambda e:e[0].usuario == usuario) \
                .filter(lambda x: self.getFrecuenciasDePalabras()[x[0].palabra] > umbral) \
                .filter(lambda x: x[1] > umbral) \
                .filter(lambda e: self.getFrecuenciasDePalabrasPorRestoDeUsuarios()[e[0]] > umbral) \
                .grouping(lambda e: e[0].palabra, \
                        lambda e:self.getImportanciaDePalabrasDeUsuario(e[0].palabra,e[0].usuario), \
                        lambda x,y: x+y)
    
    
    
    