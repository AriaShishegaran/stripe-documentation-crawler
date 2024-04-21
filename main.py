import requests
from bs4 import BeautifulSoup

# URL of the Stripe documentation page you want to scrape
url = "https://stripe.com/docs"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the elements you want to scrape using BeautifulSoup's selectors
# For example, to scrape all the links on the page:
links = soup.find_all("a")

# Process the scraped data as per your requirements
for link in links:
    href = link.get("href")
    if href is not None:
        print(href)

# You can also save the scraped data to a file or database
# For example, to save the links to a text file:
with open("links.txt", "w") as file:
    for link in links:
        href = link.get("href")
        if href is not None:
            file.write(href + "\n")
