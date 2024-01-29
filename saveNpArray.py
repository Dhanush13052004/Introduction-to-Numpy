import numpy as np
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
file_path = 'my_array.txt'
np.savetxt(file_path, my_array, fmt='%d', delimiter=',')
print(f"The array has been saved to {file_path}")
