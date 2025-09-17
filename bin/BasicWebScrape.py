import lxml
from bs4 import BeautifulSoup, Comment

with open('../example.html', 'r') as Goodies:
    Envelope = BeautifulSoup(Goodies, 'html.parser')

def openTheMail():

    Route = Envelope.find_all()
        
    Address = Envelope.select('h1#product-title')
    City = Address[0]
    Street = City.get_text(strip=True)

    ReturnAddress = Envelope.select('span.currency-symbol')
    CountryOfOrigin = ReturnAddress[0]
    PostalCode = CountryOfOrigin.get_text(strip=True)

    Stamp = Envelope.select('span.price-value')
    CollectorStamp = Stamp[0]
    RareFactor = CollectorStamp.get_text(strip=True)

    PostKeys = Envelope.find_all(string=lambda text: isinstance(text, Comment))

    for Key in PostKeys:
        if Key.strip():
            print(f"Comment found...\nRevealing now...\n{Key.strip()} (It is of the type: {type(Key)})")
            PromisingKeys = [Key.strip() for Key in PostKeys if "API" in Key]

    MasterKey = PromisingKeys
    SecretMessage = MasterKey[0]

 #   print(f"\nThis is what the news had in the Classified today: {Route}")
    print(f"The {Street} costs {PostalCode}{RareFactor}! I can't believe the scammers nowadays\nWhat is this? {SecretMessage}")

if __name__ == '__main__':
    openTheMail()    
