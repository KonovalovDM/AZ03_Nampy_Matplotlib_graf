# Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену
# и вывести ее, а также сделать гистограмму цен на диваны​

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

import csv

# URL для получения данных
url = "https://www.divan.ru/category/divany-i-kresla"

# Заголовки для обхода блокировки со стороны сайта
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Получение HTML-контента страницы
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Извлечение названий и цен диванов
sofa_data = []
for product in soup.find_all("div", class_="product-card"):  # Убедись, что класс соответствует сайту
    name = product.find("a", class_="product-card__name").text.strip()
    price = product.find("span", class_="product-card__price").text.strip().replace("₽", "").replace(" ", "")
    sofa_data.append({"Название": name, "Цена": int(price)})

# Сохранение данных в CSV файл
df = pd.DataFrame(sofa_data)
df.to_csv("divan_prices.csv", index=False)

# Вычисление средней цены
average_price = df["Цена"].mean()
print(f"Средняя цена на диваны: {average_price:.2f} ₽")

# Построение гистограммы цен
plt.figure(figsize=(10, 6))
plt.hist(df["Цена"], bins=20, color="skyblue", edgecolor="black")
plt.title("Гистограмма цен на диваны")
plt.xlabel("Цена (₽)")
plt.ylabel("Количество")
plt.grid(True)
plt.show()

# Проверка загруженных данных
print(df.head())  # Вывод первых нескольких строк для проверки структуры

if "Цена" in df.columns:
    # Если столбец "Цена" существует, вычисляем среднюю цену
    average_price = df["Цена"].mean()
    print(f"Средняя цена на диваны: {average_price:.2f} ₽")
else:
    print("Столбец 'Цена' не найден в DataFrame. Проверьте структуру данных.")
