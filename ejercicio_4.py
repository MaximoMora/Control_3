from ejercicio_3 import *

dict_row

dict_column

def add_to_dict(dict, key, value):
  dict[key] = value
   
def ord_burbuja(datos):
  new_list_value = []
  new_list_key = []
  dict = datos
  new_dict = {}
  for key, value in dict.items():
    new_list_value.append(value)
    new_list_key.append(key)
  
  datos = new_list_value
  
  for i in range(len(datos)):
    for k in range((len(datos)) - i - 1):
      if datos[k] > datos[k + 1]:
        datos[k], datos[k + 1] = datos[k + 1], datos[k]
  
  for j in range(0, len(new_list_key)):
    add_to_dict(new_dict, new_list_key[j], new_list_value[j])

  return new_dict


rowUpward = ord_burbuja(dict_row)
columnUpward = ord_burbuja(dict_column)
print(rowUpward)
print(columnUpward)
