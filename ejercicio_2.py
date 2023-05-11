import matplotlib.pyplot as plt
import numpy as np
from ejercicio_1 import * 

C1csv

def average_row(array):
    dict_average_row = {}
    average_row = np.average(array,axis=1)
    for row in range(16):
        dict_average_row[row+1] = average_row[row]
    return dict_average_row

def average_column(array):
    dict_average_column = {}
    result_reverse = np.transpose(array)
    average_column = np.average(result_reverse,axis=1)
    for row in range(16):
        dict_average_column[row+1] = average_column[row]
    return dict_average_column


dict_row = average_row(C1csv)
dict_column = average_column(C1csv)
print(dict_row)
print(dict_column)


