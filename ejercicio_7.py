from ejercicio_2 import *
from ejercicio_6 import *
import matplotlib.pyplot as plt

C1C2

C1C2_row =average_row(C1C2)
C1C2_colunm = average_column(C1C2)
print(C1C2_row)
print(C1C2_colunm)

def Show_Bar(TValue):
    E = []
    fig, ax = plt.subplots()
    for i in range(0,16):
        a = "Fila " + str(i+1) 
        E.append(a)

    p = ax.bar(E, TValue, 0.6, label=0.6, bottom=1)
    ax.bar_label(p, label_type='edge')
    plt.xlabel("Columnas")
    plt.ylabel("Valores")
    plt.title("Promedios por Columnas")
    plt.show()

Show_Bar(C1C2_row.values())
