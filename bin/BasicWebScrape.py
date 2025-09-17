import lxml
from bs4 import BeautifulSoup, Comment

with open('../example.html', 'r') as Goodies:
    Envelope = BeautifulSoup(Goodies, 'html.parser')

def openTheMail():
    counter = 0
    
    Route = Envelope.find_all()
    PostKeys = Envelope.find_all()
        
    Address = Envelope.select('h1#product-title')
    City = Address[0]
    Street = City.get_text(strip=True)

    ReturnAddress = Envelope.select('span.currency-symbol')
    CountryOfOrigin = ReturnAddress[0]
    PostalCode = CountryOfOrigin.get_text(strip=True)

    Stamp = Envelope.select('span.price-value')
    CollectorStamp = Stamp[0]
    RareFactor = CollectorStamp.get_text(strip=True)

    SecretMessage = ""

    MasterKey = Envelope.find_all(isinstance('text', Comment))

    for counter in PostKeys:
        MasterKeyCandidate = Envelope.find_all('div'),(counter)
        if MasterKey == Envelope.find_all(isinstance('text', Comment)):
            Engraving = MasterKey
            print(f"After {counter} keys I finally found it! The engraved master key!\nThe engraving on it says {Engraving}")
        else:
            Engraving = "Made you look!" 
            counter + 1 == counter
            if counter > 5:
                print(f"{counter} keys checked now I've seen a few engraved messages.\nOne of these keys might be the master key...\n Hah! {Engraving}")

 #   print(f"\nThis is what the news had in the Classified today: {Route}")
    print(f"The {Address} costs {CountryOfOrigin}{CollectorStamp}! I can't believe the scammers nowadays")
    return

if __name__ == '__main__':
    openTheMail()    
