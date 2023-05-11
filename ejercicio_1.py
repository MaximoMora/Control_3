import csv  # Se comienza con la importación de :csv: para manejar archivos :.csv:
import numpy as np  # Se importa :numpy: abreviado a :np:
                    # Numpy en este caso para trabajar con matrices

# Comenzamos definiendo la función read_csv(file_name)
# en donde file_name es un parametro para usar dentro de la funcion.
def read_csv(file_name):
  
  # Creamos una lista vacía para almacenar el resultado de la "lectura"
  result = []
  with open(file_name) as file: # Abrimos el :file_name: usando la funcion open() y lo asignamos a :file:
      reader = csv.reader(file) # Asignamos la informacion de csv.reader(file) a la variable :reader:, es decir que leemos el archivo y almacenamos el contenido en :reader:
      for i in reader:  # Creamos un loop que itere el numero de
        result.append(i)  # Almacenamos el contenido de las variables que vaya tomando :i: a la lista :result:
      result_float = np.float64(result) # Transformamos el contenido de :result: a un np.float64() y se almacena en :result_float: 
  return result_float # Se retorna el valor de :result_float:

C1csv = read_csv("C1.csv")  # Se asigna el retorno de la funcion al valor :C1csv:
print(C1csv)  # Se usa print() para la variable :C1csv: ya que contiene los valores de la funcion anterior y se muestren en pantalla
