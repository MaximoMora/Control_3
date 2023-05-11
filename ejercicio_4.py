from ejercicio_3 import * # Importamos las librerias, variables y el contenido de :ejercicio_3:

def add_to_dict(dict, key, value):  # Creamos una pequeña función que adjunte valores a un diccionario seleccionado
  dict[key] = value
   
def bubble_sort(old_dict): # Creamos la función bubble_sort
  new_list_value = [] # Definimos una lista vacía para almacenar todos los :values: de un diccionario
  new_list_key = [] # Definimos una lista vacía para almacenar todas las :keys: de un diccionario
  new_dict = {} # Creamos un diccionario vacío para almacenar los valores finales
  for key, value in old_dict.items(): # Creamos un ciclo que itere el numero de veces dependiendo del numero de items() en el diccionario
    new_list_value.append(value)new_dict  # Separamos en dos listas cada valor del diccionario
    new_list_key.append(key)
  
  value = new_list_value  # Creamos la variable :value: para trabajar con un nombre de variable mas corto  
  for i in range(len(value)): # Creamos in ciclo que itere el numero de veces del largo de elementos de :new_list_value: o :value: ambos tienen el mismo largo y son el mismo elemento
    for k in range((len(value)) - i - 1): # Hacemos otro ciclo pero que esta vez se reduzca el numero de iteraciones a medida que avanza el ciclo anterior
      if value[k] > value[k + 1]:                               # Si i es > que i+1
        value[k], value[k + 1] = value[k + 1], old_dict[k]      # Entonces hacemos un swap de posición. Los cambiamos de lugar
  for j in range(0, len(new_list_key)): #Hacemos otro ciclo para añadir los valores nuevos a el diccionario nuevo reordenado
    add_to_dict(new_dict, new_list_key[j], value[j])  # Usamos la funcion add_to_dict() para añadir los nuevos valores al nuevo diccionario.
  return new_dict # Retornamos el valor del nuevo diccionario.

rowUpward = ord_burbuja(dict_row) # Asignamos los valores de ord_burbuja(dict_row), es decir los valores ordenados a la variable rowUpward
columnUpward = ord_burbuja(dict_column) # Hacemos lo mismo pero con los valores de ord_burbuja(dict_column)
print(rowUpward) 
print(columnUpward)
