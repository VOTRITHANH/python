import numpy as np

# Tạo mảng arr
arr = np.arange(9).reshape(3, 3)

# Hiển thị mảng ban đầu
print("Mảng ban đầu:")
print(arr)

# Hoán đổi cột 0 và cột 1
arr[:, [0, 1]] = arr[:, [1, 0]]

# Hiển thị mảng sau khi hoán đổi
print("Mảng sau khi hoán đổi cột 0 và cột 1:")
print(arr)
