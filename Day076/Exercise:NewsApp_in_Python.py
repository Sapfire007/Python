"""
Objective:
Use the NewsAPI and the requests module to fetch the daily news related to different topics. Go to: https://newsapi.org/ and explore the various options to build you application.
"""


import requests
import json

query = input("Enter the type of news you want to view : ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-06-30&sortBy=publishedAt&language=en&apiKey=API_KEY"

response = requests.get(url)
news = json.loads(response.text)

# print(news, type(news))
for articles in news.get("articles"):
  print(articles.get("title"))
  print(articles.get("description"))
  print("==========================================================")