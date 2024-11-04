# 1. Создай гистограмму для случайных данных, сгенерированных с помощью функции numpy.random.normal.
# Параметры нормального распределения
# mean = 0       # Среднее значение
# std_dev = 1    # Стандартное отклонение
# num_samples = 1000  # Количество образцов
# Генерация случайных чисел, распределенных по нормальному распределению
# data = np.random.normal(mean, std_dev, num_samples)

import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('Гистограмма случайных данных (нормальное распределение)')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)
plt.show()

# 2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.​
# import numpy as np
# random_array = np.random.rand(5) # массив из 5 случайных чисел
# print(random_array)

import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 100  # Количество точек
x_data = np.random.rand(num_samples)
y_data = np.random.rand(num_samples)

# Построение диаграммы рассеяния
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, color='purple', alpha=0.5, edgecolor='black')
plt.title('Диаграмма рассеяния для двух наборов случайных данных')
plt.xlabel('Значения X')
plt.ylabel('Значения Y')
plt.grid(True)
plt.show()