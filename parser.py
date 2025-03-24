import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    with open("books.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Название", "Цена"])  # Заголовки

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            writer.writerow([title, price])  # Записываем строку в CSV

    print("Данные сохранены в books.csv")

else:
    print("Ошибка доступа:", response.status_code)