from ejercicio_2 import * #importa todo del ejercicio 2
from ejercicio_3 import * #importa todo del ejercicio 3
from ejercicio_4 import * #importa todo del ejercicio 4
from ejercicio_6 import * #importa todo del ejercicio 5

C1C2_row = average_row(C1C2) #El promedio de las filas 
C1C2_column = average_column(C1C2) #El promedio de las columnas
C1C2_row_sort = ord_burbuja(C1C2_row) #El promedio ordenado de las filas
C1C2_column_sort = ord_burbuja(C1C2_column) #El promedio ordenado de las columnas


Show_Bar(C1C2_row.values(),"Filas") #Grafico del promedio de las filas 
Show_Bar(C1C2_column.values(),"Columna") #Grafico del promedio de las columnas 
Show_Bar(C1C2_row_sort.values(),"Filas") #Grafico del promedio ordenado de las filas
Show_Bar(C1C2_column_sort.values(),"Columnas") ##El promedio ordenado de las columnas

