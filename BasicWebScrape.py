import sys
import lxml
import requests
from bs4 import BeautifulSoup, Comment

URL = 'http://quotes.toscrape.com'
HEADERS = {
    'User-Agent': 'MyFirstScraper/1.0'
}

try:
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error: Request to {URL} failed: {e}") 
    sys.exit(1)

soup = BeautifulSoup(response.text, 'lxml')

def extract_quotes(soup_object):
    quotes_list = []
    quote_containers = soup.find_all('div', class_='quote')
    for container in quote_containers:
        text_element = container.find('span', class_='text')
        author_element = container.find('small', class_='author')
        if text_element and author_element:
            quote_text = text_element.get_text(strip=True)
            author_text = author_element.get_text(strip=True)
        quotes_list.append({
            'text': quote_text,
            'author': author_text
        })
    return quotes_list

if __name__ == '__main__':
    scraped_quotes = extract_quotes(soup)

    if scraped_quotes:
        print(f"I found {len(scraped_quotes)} quotes!\n")
        for quote in scraped_quotes:
            print(f"{quote['text']} -- by: {quote['author']}")
    else:
        print(f"I couldn't find any quotes on this page:\n{URL}")
