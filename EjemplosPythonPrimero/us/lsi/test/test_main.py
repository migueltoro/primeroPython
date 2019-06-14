'''
Created on Jun 4, 2019

@author: Miuel Toro
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
    print(FIterable(r.items()).limit(100).sort())
    
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

if __name__ == '__main__':    
    test6()