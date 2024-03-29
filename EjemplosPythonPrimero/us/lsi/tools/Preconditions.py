'''
* Checks that the boolean is true. Use for validating arguments to methods.
* @param message A message
* @param condition A condition
'''
def checkArgument(condition,message=None):    
    if(not condition):
        raise Exception(message)

'''
* Checks some state of the object, not dependent on the method arguments. 
* @param message Mensaje a imprimir
* @param condition A condition
'''
def checkState(condition,message):
    if(not condition):
        raise Exception(message)
       
'''
Checks that the value is not null. 
Returns the value directly, so you can use checkNotNull(value) inline.
T El tipo del elemento    
reference Parametro a comprobar
El parametro a comprobar
'''
   
def checkNotNull(reference):
    if(not reference):
        raise Exception("Es nulo %s".format(reference))
    return reference
        
'''
* Checks that index is a valid element index into a list, string, or array with the specified size. 
* An element index may range from 0 inclusive to size exclusive. 
* You don't pass the list, string, or array directly; you just pass its size. 
* @param index Un indice 
* @param size El tamanyo de la lista
* @return Index El indice del elemento
'''
   
def checkElementIndex(index,size):
    if(not (index>=0 and index<size)):
        raise Exception("Index = %d, size %d".format(index,size))
    return index
    
'''
* Checks that index is a valid position index into a list, string, or array with the specified size. 
* A position index may range from 0 inclusive to size inclusive. 
* You don't pass the list, string, or array directly; you just pass its size. Returns index.
* @param index El indice del elemento
* @param size El tamanyo de la lista
* @return Index El indice del elemento
'''
def checkPositionIndex(index,size):
    if(not (index>=0 and index<=size)):
        raise Exception("Index = %d, size %d".format(index,size))
    return index
    