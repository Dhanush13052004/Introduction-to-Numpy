import numpy as np
array_with_missing_data = np.array([1.0, 2.0, np.nan, 4.0, np.nan, 6.0, 7.0, np.nan])
missing_data_indices = np.isnan(array_with_missing_data)
print("Original array with missing data:")
print(array_with_missing_data)
print("\nIndices of missing data:")
print(missing_data_indices)
print("\nValues of missing data:")
print(array_with_missing_data[missing_data_indices])