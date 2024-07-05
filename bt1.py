import numpy as np

# Nhập giá trị n từ bàn phím
n = int(input("Nhập số n: "))

# Tạo numpy array từ 0 đến n-1
arr = np.arange(n)

# Thay thế các giá trị lẻ bằng -1
arr[arr % 2 == 1] = -1

# In ra màn hình
print(arr)
