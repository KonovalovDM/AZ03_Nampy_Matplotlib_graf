# AZ03_Nampy_Matplotlib_graf
 ___Nampy_Matplotlib_graf___
 
## Создание гистограммы для случайных данных, сгенерированных с помощью функции `numpy.random.normal`.
___файл main.py___
### Заданные параметры нормального распределения
mean = 0 # Среднее значение
std_dev = 1 # Стандартное отклонение
num_samples = 1000 # Количество образцов

### Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

## Построение диаграммы рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.​
import numpy as np
random_array = np.random.rand(5) # массив из 5 случайных чисел
print(random_array)

## Парсинг цен диванов с сайта divan.ru в csv файл,<br> обработка данных, определение средней цены и вывод ее.
## Построение гистограммы спарсенных цен на диваны.
___файл task3.py___