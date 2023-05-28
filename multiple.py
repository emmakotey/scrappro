import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.flipkart.com"

re = requests.get(url)

print(re)

soup = BeautifulSoup(re.text, "lxml")
print(soup.encode('utf-8'))