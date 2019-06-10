'''
Created on Jun 5, 2019

@author: Miguel Toro
'''
from us.lsi.tools import FileTools
from us.lsi.tools import StringTools

def lineChart(fileOut,title,campos,datos):  
    result = FileTools.text('../../../resources/LineChartPattern.html');
    camposText = '[{0}]'.format(','.join("'"+x+"'" for x in campos));
    dataText = '{0}\n'.format(',\n'.join(filaLineChart(e,datos) for e in range(len(datos[0]))))
    reglas = {"title":"'"+title+"'", "campos":camposText, "data":dataText}
    result = StringTools.transform(result,reglas);
    FileTools.write(fileOut,result);
    
def filaLineChart(e,datos):
    return '[{0}]'.format(','.join(str(datos[i][e]) for i in range(len(datos))))
    
def pieChart(fileOut,title,campos,nombres,datos):
    pass
    
def filaPieChart(e,nombres,datos):
    pass
 
def columnsBarChart(fileOut,title,nombresDatos,nombresColumna,datos):
    pass
 
def columnaColumnsBarChart(e,nombresColumna,datos):
    pass

if __name__ == '__main__':
    pass