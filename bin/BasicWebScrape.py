import lxml
from bs4 import BeautifulSoup, Comment

with open('../example.html', 'r') as Goodies:
    Envelope = BeautifulSoup(Goodies, 'html.parser')

def openTheMail():

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
