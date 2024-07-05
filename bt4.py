import numpy as np

a = np.array([2, 6, 1, 9, 10, 3, 27])

# Lọc các phần tử nằm trong khoảng từ 5 đến 10
filtered_elements = a[(a >= 5) & (a <= 10)]

# In ra phần tử đã lọc
print(filtered_elements)
