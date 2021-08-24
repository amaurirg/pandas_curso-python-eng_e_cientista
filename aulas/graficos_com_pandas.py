import pandas as pd
import matplotlib.pyplot as plt


file_path = '../PONTOS_ESFERA.txt'
file_data = pd.read_csv(file_path, header=None, usecols=[3, 4, 5])
# print(file_data.head())

x = [i for i in file_data[3]]
y = [i for i in file_data[4]]
z = [i for i in file_data[5]]
# print(x)
# print(y)
# print(z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
plt.show()
