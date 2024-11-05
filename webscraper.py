import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://quotes.toscrape.com"

def scrape_quotes(url):
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all quote elements
        quotes = soup.find_all('div', class_='quote')
        
        # Extract and print the text of each quote and its author
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            print(f"Quote: {text}\nAuthor: {author}\n")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# Run the scraping function
scrape_quotes(url)
