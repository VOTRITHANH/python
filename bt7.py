import numpy as np

# URL của dữ liệu
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Đọc dữ liệu từ URL và bỏ qua cột cuối cùng
data = np.genfromtxt(url, delimiter=',', usecols=(0, 1, 2, 3))

# Lấy cột đầu tiên (sepallength)
sepallength = data[:, 0]

# Tính giá trị mean, median, standard deviation
mean_sepallength = np.mean(sepallength)
median_sepallength = np.median(sepallength)
std_sepallength = np.std(sepallength)

# In ra kết quả
print(f"Mean của sepallength: {mean_sepallength}")
print(f"Median của sepallength: {median_sepallength}")
print(f"Standard Deviation của sepallength: {std_sepallength}")
