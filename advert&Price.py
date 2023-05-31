import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://jiji.com.gh/"
response = requests.get(url)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, "html.parser")

# Find all "div" elements with class "b-trending-card__title"
div_elements = soup.find_all("div", class_="b-trending-card__title")

# Open a file to write the output
with open("output.txt", "w", encoding="utf-8") as file:
    # Iterate over the "div" elements and extract the text from the "div" with class "b-trending-card__price"
    for div in div_elements:
        try:
            title = div.text.strip()
            price_div = div.find_next_sibling("div", class_="b-trending-card__price")
            price = price_div.text.strip() if price_div else "No price available"

            # Write the output to the file
            file.write(f"Title: {title}\n")
            file.write(f"Price: {price}\n")
            file.write("\n")
        except UnicodeEncodeError:
            file.write(f"Title: {title.encode('ascii', 'ignore').decode('ascii')}\n")
            file.write(f"Price: {price.encode('ascii', 'ignore').decode('ascii')}\n")
            file.write("\n")

print("Scraping complete. Check the output.txt file for results.")
