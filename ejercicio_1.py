import csv
import numpy as np

def read_csv(file_name):
  result = []
  with open(file_name) as file:
      reader = csv.reader(file)
      for i in reader:
        result.append(i)

      result_float = np.float64(result)


  return result_float

C1csv = read_csv("C1.csv")
print(C1csv)
