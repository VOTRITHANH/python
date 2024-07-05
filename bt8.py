#Min-max normalization (còn gọi là min-max scaling) là một phương pháp chuẩn hóa dữ liệu,
#trong đó các giá trị được chuyển đổi để nằm trong một khoảng nhất định, thường là từ 0 đến 1.
import numpy as np

# URL của dữ liệu
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Đọc dữ liệu từ URL và bỏ qua cột cuối cùng
data = np.genfromtxt(url, delimiter=',', usecols=(0, 1, 2, 3))

# Lấy cột đầu tiên (sepallength)
sepallength = data[:, 0]

# Tính giá trị min và max của sepallength
min_sepallength = np.min(sepallength)
max_sepallength = np.max(sepallength)

# Thực hiện min-max normalization
normalized_sepallength = (sepallength - min_sepallength) / (max_sepallength - min_sepallength)

# In ra kết quả
print("Sepallength ban đầu:")
print(sepallength)
print("\nSepallength sau khi normalized:")
print(normalized_sepallength)
