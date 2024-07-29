import requests
from bs4 import BeautifulSoup

url = "https://sapfire007.github.io/WebDev/DIY_HTML_Project4-Simple_Netflix_clone_built_on_HTML&CSS/"
r = requests.get(url)
# print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for spanTexts in soup.find_all("span"):
  print(spanTexts.text)