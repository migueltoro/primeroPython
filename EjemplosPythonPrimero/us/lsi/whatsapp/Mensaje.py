'''
Created on Jun 19, 2019

@author: Miguel Toro
'''


from datetime import datetime
import re

class Mensaje:
    '''
    classdocs
    '''

    def __init__(self,fecha,hora,usuario,texto):
        '''
        Constructor
        '''
        self.fecha = fecha
        self.hora = hora
        self.usuario = usuario
        self.texto = texto
        
    
    @staticmethod  
    def of(fecha,hora,usuario,texto):
        return Mensaje(fecha, hora, usuario, texto)

    RE = r'(?P<fecha>\d\d?/\d\d?/\d\d?) (?P<hora>\d\d?:\d\d) - (?P<usuario>[^:]+): (?P<texto>.+)'
    
    @staticmethod  
    def parse(mensaje):
        matches = re.match(Mensaje.RE,mensaje)
        if(matches):
            fecha = datetime.strptime(matches.group('fecha'), '%d/%m/%y').date()
            hora = datetime.strptime(matches.group('hora'), '%H:%M').time()
            usuario = matches.group('usuario')
            texto = matches.group('texto')
            return Mensaje(fecha, hora, usuario, texto)
        else:
            return None

    
    def __str__(self):
        return "%s--%s  %10s\n  %s" % (self.fecha,self.hora,self.usuario,self.texto)
    