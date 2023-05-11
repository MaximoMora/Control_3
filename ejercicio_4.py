
dict_row = {1: 0.5, 2: 0.61875, 3: 0.346875, 4: 0.375, 5: 0.45625, 6: 0.58125, 7: 0.5843750000000001, 8: 0.47500000000000003, 9: 0.41875, 10: 0.3125, 11: 0.525, 12: 0.32187499999999997, 13: 0.49687499999999996, 14: 0.29374999999999996, 15: 0.521875, 16: 0.478125}

dict_column = {1: 0.6187499999999999, 2: 0.49999999999999994, 3: 0.34687500000000004, 4: 0.38750000000000007, 5: 0.45624999999999993, 6: 0.5812499999999998, 7: 0.5843750000000001, 
8: 0.4749999999999999, 9: 0.41874999999999996, 10: 0.29999999999999993, 11: 0.5249999999999999, 12: 0.321875, 13: 0.496875, 14: 0.29375, 15: 0.521875, 16: 0.478125}  


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


rowUpward =ord_burbuja(dict_row)
columnUpward = ord_burbuja(dict_column)
print(rowUpward)
print(columnUpward)
