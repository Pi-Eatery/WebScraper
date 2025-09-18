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

soup = BeautifulSoup(response.text, 'html.parser')

def openTheMail():
    Counter = 0
    Address = soup.find_all('div', class_='quote')
    for Family in Address:
        Household = Family.find('span', class_='text')
        FullName = Family.find('small', class_='author')
        Message = Household.get_text(strip=True)
        LastName = FullName.get_text(strip=True)
        AddressBook = print(f"\nI found a quote:\n {Message} -- by: {LastName}")

if __name__ == '__main__':
    openTheMail()
