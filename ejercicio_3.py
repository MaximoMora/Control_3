import matplotlib.pyplot as plt

from ejercicio_2 import *

def Show_Bar(TValue)
    E = []
    fig, ax = plt.subplots()
    for i in range(0,16):
        a = "Fila " + str(i+1) 
        E.append(a)

    p = ax.bar(E, TValue)
    ax.bar_label(p, label_type='edge')
    plt.xlabel("Columnas")
    plt.ylabel("Valores")
    plt.title("Promedios por Columnas")
    plt.show()

plt.bar()
plt.show()
