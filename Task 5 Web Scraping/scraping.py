import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = []
for item in soup.find_all("article", class_="product_pod"):
    title = item.h3.a["title"]
    price = item.find("p", class_="price_color").get_text(strip=True)
    books.append([title, price])

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price"])
    writer.writerows(books)

print("Book data saved to books.csv")