import pandas as pd

# Загружаем данные
df = pd.read_csv("books.csv",encoding="utf-8")

# Выводим первые 5 строк
print(df.head())

# Проверяем типы данных

# Преобразуем цены в числа (убираем символы £)
df["Цена"] = df["Цена"].str.replace(r"[^\d.]", "",regex= True).astype(float)

# Выводим статистику по ценам
print(df.describe())