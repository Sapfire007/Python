import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com/my-gear/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

productsListed = soup.find_all("h2",class_="title-font mt-5 text-xl font-medium text-gray-900 dark:text-gray-100")
productLinks = soup.find_all("a",class_="my-1 mr-2 inline-flex w-fit cursor-pointer items-center rounded-full bg-purple-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-lg transition ease-in-out hover:scale-105 hover:bg-purple-800")

for index, (product,links) in enumerate(zip(productsListed,productLinks)):
  currentLink = links.get("href")
  with open("Day084/scrapedProducts.txt","a") as f:
    f.write(f"{index+1}. {product.text.strip()} - {currentLink}"+"\n")
  # print(f"({index+1}. {product.text.strip()} - {currentLink}")