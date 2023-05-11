from ejercicio_1 import * #importa todo de ejercicio_1
import numpy as np #importa la libreia numpy como np

C2csv = read_csv("C2.csv") #Lee el archivo C2csv con la funcion read_csv() que devuelve la matrix en flotante
print(C2csv) #imprime el resultado de la matrix

C1C2 = C1csv * C2csv #Hace una multiplicacion matricial

print(C1C2)
