import numpy as np

# URL của dữ liệu
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Đọc dữ liệu từ URL và bỏ qua cột cuối cùng
data = np.genfromtxt(url, delimiter=',', usecols=(0, 1, 2, 3))

# Hiển thị kết quả
print(data)
