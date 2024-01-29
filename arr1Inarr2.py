import numpy as np
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([3, 5, 7, 9])
result = np.isin(array1, array2)
print("Array 1:", array1)
print("Array 2:", array2)
print("Result (Is each element of array1 present in array2?):", result)
