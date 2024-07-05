import numpy as np

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

# Tìm phần tử chung giữa hai mảng
common_elements = np.intersect1d(a, b)

# In ra phần tử chung
print(common_elements)
