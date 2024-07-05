import numpy as np
# Tạo các mảng nhỏ
first_row = np.arange(5)  # Tạo mảng từ 0 đến 4
second_row = np.arange(5, 10)  # Tạo mảng từ 5 đến 9
third_row = np.ones(5, dtype=int)  # Tạo mảng chứa toàn số 1 với độ dài 5

# Kết hợp các mảng nhỏ lại thành một mảng lớn
result = np.vstack([first_row, second_row, third_row, third_row])

# In ra mảng kết quả
print(result)
