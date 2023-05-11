from ejercicio_1 import *   #   Importamos todo del :ejercicio_1.py: 
                            #   Es decir las librerias numpy y import numpy as npimport numpy as np
    
def average_row(array): #   Creamos una función, esta calculará la media aritmetica de las filas.
    #   El resultado se almacenará en un diccionario, de momento se creará uno vacío llamado :dict_average_row:
    dict_average_row = {}
    average_row = np.average(array,axis=1)  #   Usamos numpy.average() con axis=0 para calcular el promedio de las filas
    count_row, count_column = array.shape   #   Se calcula el numero de columnas y filas para el ciclo for de columnas y filas
    
    for row in range(count_row): #   El ciclo itera el numero de veces dependiendo de el numero de filas de la matriz
        dict_average_row[row+1] = average_row[row]  #   Ahora el promedio se almacenará en el diccionario creado anteriormente
        #   El diccionario almacenará {"key": value}
        #   En donde la :key: es el numero de la columna
        #   Y el :value: es el valor de la media aritmetica de esa columna
    return dict_average_row  #   Retorna el valor del diccionario para que pueda ser usado

def average_column(array):
    dict_average_column = {}    #   El resultado se almacenará en un diccionario :dict_average_column:
    average_column = np.average(result_reverse,axis=0)  #   Usamos numpy.average() con axis=1 para calcular el promedio de las filas
    count_row, count_column = array.shape
    
    for column in range(count_column): #   El ciclo itera el numero de veces dependiendo de el numero de columnas de la matriz
        dict_average_column[column+1] = average_column[column]  #   Lo mismo que la anterior función, se almacena el contenido en el diccionario
    return dict_average_column  #   Retorna el valor del diccionario para que pueda ser usado

dict_row = average_row(C1csv)   #   Asignamos los valores de las filas a :dict_row:
dict_column = average_column(C1csv)   #   Asignamos los valores de las columna a :dict_column:
print(dict_row) #   Hacemos :print: del resultado
print(dict_column)


