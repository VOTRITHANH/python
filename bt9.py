import numpy as np

# URL của dữ liệu
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Đọc dữ liệu từ URL và bỏ qua cột cuối cùng
data = np.genfromtxt(url, delimiter=',', usecols=(0, 1, 2, 3))

# Lọc các dòng có petallength > 1.5 và sepallength < 5.0
filtered_data = data[(data[:, 2] > 1.5) & (data[:, 0] < 5.0)]

# In ra kết quả
print("Các dòng có petallength > 1.5 và sepallength < 5.0:")
print(filtered_data)
