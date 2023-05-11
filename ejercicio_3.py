import matplotlib.pyplot as plt

from ejercicio_2 import *

def Show_Bar(TValue) 
    E = []                              #variable donde se guardaran los nombres de las filas
    fig, ax = plt.subplots()            #funcion que crea subtrazos
    for i in range(0,len(TValue)):      #For para añadir los nombres a las barras
        a = "Fila " + str(i+1)          
        E.append(a)

    p = ax.bar(E, TValue)               #poner en las barras el Nombre de lista y Valores
    ax.bar_label(p, label_type='edge')  #centrarlos y acomodarlos
    plt.xlabel("Columnas")              
    plt.ylabel("Valores")
    plt.title("Promedios por Columnas")
    fig.set_size_inches(18.5, 10.5)     #para que la figuras salgan grandes a la hora de ejecutar
    plt.show()

plt.bar()
plt.show()
