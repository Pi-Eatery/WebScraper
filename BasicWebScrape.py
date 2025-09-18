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

Envelope = BeautifulSoup(response.text, 'html.parser')

def openTheMail():
    Counter = 0
    Address = Envelope.find_all('div', class_='quote')
    for Family in Address:
        Household = Family.find('span', class_='text')
        FullName = Family.find('small', class_='author')
        Message = Household.get_text(strip=True)
        LastName = FullName.get_text(strip=True)
        AddressBook = print(f"\nI found a quote:\n {Message} -- by: {LastName}")


def sendTheMail(): # Concept in static action (auto runs if the status code of the requested webpage isn't 200)

    Address = Envelope.select('h1#product-title')
    City = Address[0]
    Street = City.get_text(strip=True)

    ReturnAddress = Envelope.select('span.currency-symbol')
    Stamp = Envelope.select('span.price-value')
    CountryOfOrigin = ReturnAddress[0]
    CollectorStamp = Stamp[0]
    PostalCode = CountryOfOrigin.get_text(strip=True)
    RareFactor = CollectorStamp.get_text(strip=True)

    Phone = Envelope.find_all('li')
    for Name in Phone:
        if "SKU:" in Name.get_text():
            MailManName = Name.get_text()
            break

    PostKeys = Envelope.find_all(string=lambda text: isinstance(text, Comment))
    for Key in PostKeys:
        if "API" in Key:
            print(f"API KEY FOUND EXPOSED\nRESOLVE SECURITY VULNERABILITY IMMEDIATELY")
        else:
            print(f"Comment found...\nRevealing now...\n{Key.strip()} (This comment is this type: {type(Key)})")

    print(f"Found {Street} ({MailManName}) for {PostalCode}{RareFactor}")

if __name__ == '__main__':
    openTheMail()
