from ejercicio_2 import *
from ejercicio_3 import *
from ejercicio_4 import *
from ejercicio_6 import *
import matplotlib.pyplot as plt 

C1C2_row = average_row(C1C2)
C1C2_column = average_column(C1C2)
C1C2_row_sort = ord_burbuja(C1C2_row)
C1C2_column_sort = ord_burbuja(C1C2_column)


Show_Bar(C1C2_row.values(),"Filas")
Show_Bar(C1C2_column.values(),"Columna")
Show_Bar(C1C2_row_sort.values(),"Filas")
Show_Bar(C1C2_column_sort.values(),"Columnas")
