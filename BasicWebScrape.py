import lxml
import requests
from bs4 import BeautifulSoup, Comment

headers = {'User-Agent': 'MyFirstScraper/1.0'}

#
#       For Static pages replace 'downloads/pages/example.html' 
#       with your file's path from the root of this repo
#       then uncomment it's line and the line after it
#
Ink = requests.get('http://quotes.toscrape.com')
if Ink.status_code == 200:
    with open('downloads/pages/requested.html', 'w') as BlankLetter:
        print(Ink.text, file=BlankLetter)
    with open('downloads/pages/requested.html', 'r') as FullLetter:
        Envelope = BeautifulSoup(FullLetter, 'html.parser')
else:
    with open('downloads/pages/example.html', 'r') as Goodies:
        Envelope = BeautifulSoup(Goodies, 'html.parser')

def openTheMail():
    AddressBook = []
    Country = Envelope.find_all()
    for State in Country:
        Address = Envelope.find_all('div.quote')
        print(Address)
        for Person in Address:
            AddressBook.append(Person.get_text())
    print(f"The quotes I could find were:\n {AddressBook}")


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
    if Ink.status_code == 200:
        openTheMail()
    else:
        sendTheMail()    
