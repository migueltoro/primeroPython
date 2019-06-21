'''
Created on Jun 18, 2019

@author: Miguel Toro
'''


from enum import Enum
from abc import abstractmethod
from us.lsi.data.coordenadas2D import Coordenadas2D
from us.lsi.tools.FIterable import FIterable
from us.lsi.tools import FileTools
from us.lsi.tools import StringTools

class GraphicType(Enum):
    Bing = 0
    Google = 1


class AbstractGraphicsMap():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(AbstractGraphicsMap, self).__init__()

    @abstractmethod
    def toPoint(self,coordenadas):
        pass
    @abstractmethod
    def toMarker(self,color, text, coordenadas):
        pass
    @abstractmethod
    def getKey(self):
        pass
    @abstractmethod
    def getPolylinePattern(self):
        pass
    @abstractmethod
    def getMarkersPattern(self):
        pass
    
    def polyline(self,fileOut, ubicaciones):
        center = Coordenadas2D.center(ubicaciones)
        result = self.getPolylinePattern()
        polylineText = FIterable(ubicaciones).map(lambda x: self.toPoint(x)).joining(",\n","\n[", "]\n")
        centerText = self.toPoint(center)
        markerCenterText = self.toMarker("red","C",center)
        markerBeginText = self.toMarker("red","S",ubicaciones[0])
        markerEndText = self.toMarker("red","E",ubicaciones[len(ubicaciones)-1])
        keyText = self.getKey()
        reglas = {"center":centerText, "markerbegin": markerBeginText,"markerend":markerEndText, \
                  "markercenter":markerCenterText,"polyline":polylineText,"key":keyText}
        result = StringTools.transform(result,reglas)
        FileTools.write(fileOut,result)

    def markers(self,fileOut, markerColor, ubicaciones):
        center = Coordenadas2D.center(ubicaciones)
        result = self.getMarkersPattern()
        markersText = FIterable(ubicaciones).map(lambda x: self.toMarker(markerColor,"E",x)).joining("\n","\n", "\n")
        centerMarkerText = self.toMarker("red","C",center)
        centerText = self.toPoint(center);
        keyText = self.getKey()
        reglas = {"center":centerText,"markercenter":centerMarkerText,"markers":markersText,"key":keyText}
        result = StringTools.transform(result,reglas);
        FileTools.write(fileOut,result)
        

class GraphicsBingMap(AbstractGraphicsMap):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(GraphicsBingMap, self).__init__()
    
    @staticmethod 
    def of():
        return GraphicsBingMap()

    m = -1;
    
    def toPoint(self,coordenadas):
        return "new Microsoft.Maps.Location(%f,%f)" % (coordenadas.latitude,coordenadas.longitude)

    def toMarker(self,color,text,coordenadas):
        lat = '{0:.6f}'.format(coordenadas.latitude)
        lng = '{0:.6f}'.format(coordenadas.longitude)
        GraphicsBingMap.m = GraphicsBingMap.m+1
        n = GraphicsBingMap.m
        return '''var pin%d = new Microsoft.Maps.Pushpin(new Microsoft.Maps.Location(%s,%s), { 
                color: '%s',
                text: '%s'
                });
                map.entities.push(pin%d);''' % (n,lat,lng,color,text,n)
    
    def getKey(self):
        return FileTools.lineas("../../../resources/privateBing.txt")[0]

    def getPolylinePattern(self):
        return FileTools.text("../../../resources/BingPolylinePattern.html")

    def getMarkersPattern(self):
        return FileTools.text("../../../resources/BingMarkersPattern.html")
    

class GraphicsGoogleMap(AbstractGraphicsMap):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(GraphicsGoogleMap, self).__init__() 
        
    @staticmethod 
    def of():
        return GraphicsGoogleMap()
    
    m = -1;
    
    def toMarker(self,color,text,coordenadas):
        url = "\"http://maps.google.com/mapfiles/ms/icons/"
        url += color + "-dot.png\""
        lat = '{0:.6f}'.format(coordenadas.latitude)
        lng = '{0:.6f}'.format(coordenadas.longitude)
        GraphicsGoogleMap.m = GraphicsGoogleMap.m+1
        n = GraphicsGoogleMap.m
        return '''marker%d = new google.maps.Marker({\r\n 
                    map: map,\r\n 
                    position: {lat: %s, lng: %s},\r\n 
                    title: '%s' ,\r\n
                    icon: {\r\n url: " + url+ "}\r\n 
                  });''' % (n,lat,lng,text)

    def toPoint(self, coordenadas):
        lat = '{0:.6f}'.format(coordenadas.latitude)
        lng = '{0:.6f}'.format(coordenadas.longitude)
        return "{lat: %s, lng: %s}" % (lat,lng)

    def getKey(self):
        return FileTools.lineas("../../../resources/privateGoogle.txt")[0]

    def getPolylinePattern(self):
        return FileTools.text("../../../resources/GooglePolylinePattern.html")
    
    def getMarkersPattern(self):
        return FileTools.text("../../../resources/GoogleMarkersPattern.html")  


class GraphicsMap:
    
    def __init__(self):
        '''
        Constructor
        '''
    bm = GraphicsBingMap.of()
    gm = GraphicsGoogleMap.of()
    
    types = {GraphicType.Bing: bm, GraphicType.Google: gm}
    
    @staticmethod
    def of(tipo):
        g = GraphicsMap.types[tipo]
        return g
    
