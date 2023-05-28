import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://subslikescript.com/movies"
response = requests.get(url)

# Create a BeautifulSoup object with the website's HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Locate the elements with tag "ul" and class "scripts-list"
ul_elements = soup.find_all('ul', class_='scripts-list')

# Scrape and print the text attributes of "a" elements inside the "ul" elements
for ul_element in ul_elements:
    a_elements = ul_element.find_all('a')
    for a_element in a_elements:
        print(a_element.text)