import sys
import lxml
import requests
from bs4 import BeautifulSoup, Comment

def get_html_page(URL, HEADERS):
    response = requests.get(URL, headers=HEADERS)
    return response

def extract_quotes(soup_object):
    quotes_list = []
    quote_containers = soup_object.find_all('div', class_='quote')
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


def find_next_link(soup_object):
    button_containers = soup_object.find_all('ul', class_='pager')
    for container in button_containers:
        button_element = container.find('li', class_='next')
        if button_element:
            clickable_button = button_element.find('a')
            url_sub = clickable_button['href']
            return url_sub
        else:
            print(f"Last page scraped!")

if __name__ == '__main__':
    original_url = 'http://quotes.toscrape.com'
    url_to_scrape = original_url
    ethical_headers = {
        'User-Agent': 'MyFirstScraper/1.0'
    }
    quote_master_list = []
    while url_to_scrape != None:
        print(url_to_scrape)
        page_to_scrape = get_html_page(url_to_scrape, ethical_headers)
        soup = BeautifulSoup(page_to_scrape.text, 'lxml')
        scraped_quotes = extract_quotes(soup)
        quote_master_list.extend(scraped_quotes)
        url_sub = find_next_link(soup)
        if url_sub != None:
            url_to_scrape = original_url + url_sub
        else:
            url_to_scrape = None


    if scraped_quotes:
        print(f"I found {len(quote_master_list)} quotes!\n")
        for quote in quote_master_list:
            print(f"{quote['text']} -- by: {quote['author']}")
    else:
        print(f"I couldn't find any quotes on this page:\n{URL}")
