import numpy as np
import random

# URL của dữ liệu
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Đọc dữ liệu từ URL và bỏ qua cột cuối cùng
data = np.genfromtxt(url, delimiter=',', usecols=(0, 1, 2, 3))

# Thiết lập số lượng giá trị sẽ thay thế bằng np.nan
num_nan = 10  # Số lượng giá trị sẽ thay thế bằng np.nan

# Thay thế ngẫu nhiên các giá trị bằng np.nan
for _ in range(num_nan):
    i = random.randint(0, data.shape[0] - 1)
    j = random.randint(0, data.shape[1] - 1)
    data[i, j] = np.nan

print("Dữ liệu sau khi thay thế các giá trị ngẫu nhiên bằng np.nan:")
print(data)

# Thay thế các giá trị np.nan bằng 0
data = np.nan_to_num(data)

print("\nDữ liệu sau khi thay thế np.nan bằng 0:")
print(data)
