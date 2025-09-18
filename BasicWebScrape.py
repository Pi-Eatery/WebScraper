import sys
import csv
import lxml
import time
import requests
from bs4 import BeautifulSoup, Comment


BASE_URL = 'http://quotes.toscrape.com'

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
    button_element = soup_object.find('li', class_='next')
    if button_element:
        clickable_button = button_element.find('a')
        if clickable_button and 'href' in clickable_button.attrs:
            url_sub = clickable_button['href']
            return url_sub
    else:
        print(f"Last page scraped!")

def save_to_csv(quotes_list, filename="quotes.csv"):
    headers = ['text', 'author']

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(quotes_list)
    

if __name__ == '__main__':
    url_to_scrape = BASE_URL
    ethical_headers = {
        'User-Agent': 'MyFirstScraper/1.0'
    }
    quote_master_list = []
    while url_to_scrape:
        print(f"Scraping page: {url_to_scrape}")
        page_to_scrape = get_html_page(url_to_scrape, ethical_headers)
        if not page_to_scrape:
            break

        soup = BeautifulSoup(page_to_scrape.text, 'lxml')
        scraped_quotes = extract_quotes(soup)
        quote_master_list.extend(scraped_quotes)
        url_sub = find_next_link(soup)
        if url_sub:
            url_to_scrape = BASE_URL + url_sub
            time.sleep(1)
        else:
            print(f"No more pages to scrape!")
            url_to_scrape = None

    if quote_master_list:
        save_to_csv(quote_master_list)
        print(f"I found {len(quote_master_list)} quotes!\n")
        print(f"Data saved to quotes.csv")
    else:
        print(f"Scraping failed...\nI couldn't find any quotes on this page:\n{URL}")
