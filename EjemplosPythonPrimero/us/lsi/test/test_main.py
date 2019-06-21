'''
Created on Jun 4, 2019

@author: Miguel Toro
'''
from us.lsi.data.coordenadas2D import Coordenadas2D
from us.lsi.data.coordenadas3D import Coordenadas3D
from us.lsi.ruta.Marca import Marca
from us.lsi.ruta.Ruta import Ruta
from us.lsi.tools import FileTools
from us.lsi.tools import StringTools
from us.lsi.palabras import Palabras
from us.lsi.sevici.Estacion import Estacion
from us.lsi.sevici.Red import Red
from us.lsi.sevici.Redes import Redes
from us.lsi.tools.FIterable import FIterable
import operator
from us.lsi.montecarlo.Card import Card
from us.lsi.montecarlo.Mano import Mano
from us.lsi.tools.GraphicsMap import GraphicType
from us.lsi.whatsapp.Mensaje import Mensaje
from us.lsi.whatsapp.Grupo import Grupo

def test1():
    
    sevilla = Coordenadas2D(37.3828300, -5.9731700)
    cadiz = Coordenadas2D(36.5008762, -6.2684345)
    print(sevilla.distance(cadiz)) 
    c1 = Coordenadas3D(36.74991256557405,-5.147951105609536,0.7122000122070312)
    c2 = Coordenadas3D(36.75008556805551,-5.148005923256278,0.7127999877929688)
    d1 = c1.to2D()
    d2 = c2.to2D()
    print(c1)
    print(c2)
    print(d1)
    print(d2)
    print(c1.to2D().esCercana(c2.to2D(), 3.4))
    print(c1.to2D().distance(c2.to2D()))
    print(c1.distance(c2))
    
def test2():
    m = Marca.parse('00:00:00,36.74991256557405,-5.147951105609536,712.2000122070312')
    print(m)
    
def test3():
    r = Ruta.ofFile('../../../resources/ruta.csv')
    print(r.velocidad())
    
def test4():
    text = FileTools.text('../../../resources/PieChartPattern.html')
#    print(text)
    print(StringTools.transform(text,{'data': 'Antonio', 'campos': 'Juan'}))
    
def test5():
    r = Ruta.ofFile('../../../resources/ruta.csv')
    r.mostrarAltitud('../../../ficheros/alturas.html')
    
def test6():
    r = Palabras.gruposDeLineas('../../../resources/quijote.txt')
    print(FIterable(r.items()).sort().limit(100))
    
def test7():
    e = Estacion.parse('149_CALLE ARROYO,20,11,9,37.397829929383,-5.97567172039552'.split(','))
    print(e)
    
def test8():
    r = Red.ofFile()
    print(r)
    
def test9():
    r = Red.of('/v2/networks/sevici')
    ubicacion = r.estaciones[0].ubicacion
    print(FIterable(r.cercanas(ubicacion,0.9)))
    
def test10():
    r = Redes.ofUrl()
    StringTools.to_unicode(r)
    
def test11():
    r = Redes.ofUrl()
    print(FIterable(r.allByCountry('ES')).distinct().map(lambda x: x.href).sort())
       
def test12():
    r = FIterable.range(1, 100, 2).reduce(operator.add,operator.mul)
    print(r)
    
def test13():
    r = FIterable.range(1, 100, 2).estadisticos()
    print(r.sum)
    print(r.desviacion_tipica())
    
def test14():
    c = Card.ofText('10D')
    print(c)
    
def test15():
    m1 = Mano.random()
    m2 = Mano.ofText('[10D,10H,10C,10S,5H]')
#    print(m.fuerza())
    print(m1< m2)
    print(m1)
    print(m2)
    print(m1.getFuerza())
    print(m2.getFuerza())
    m1.toGraphics('../../../ficheros/CartasOut.html')
    
def test16():
    r = Ruta.ofFile('../../../resources/ruta.csv')
    r.mostrarMapa('../../../ficheros/GoogleMapaOut.html',GraphicType.Google)

def test17():
    m = Mensaje.parse('26/2/16 9:16 - Leonard: De acuerdo, ¿cuál es tu punto?')
    print(m)
    g = Grupo.ofFile('../../../resources/bigbangtheory_es.txt')
    print(StringTools.to_unicode(g))
    
def test18():
    g = Grupo.ofFile('../../../resources/bigbangtheory_es.txt')
#    print(len(g.getMensajes()))
#    g.drawNumeroDeMensajesPorDiaDeSemana('../../../ficheros/DiaSemanaOut.html')
##    ms = g.getImportanciaDePalabrasDeUsuario('Leonard', 'gato')
    ms = g.getPalabrasCaracteristicasDeUsuario('Leonard',3)
#    print(ms)
    print(FIterable(ms.items()).sort(lambda x: x[1],reverse=True))
#    print(FIterable(g.getMensajesPorUsuario()))
#   print(ms)

if __name__ == '__main__':    
    test18()