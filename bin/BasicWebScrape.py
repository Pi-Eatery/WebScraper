import lxml
from bs4 import BeautifulSoup, Comment

with open('../example.html', 'r') as Goodies:
    Envelope = BeautifulSoup(
        Goodies, 
        'html.parser'
    )

def openTheMail():
    counter = 0
    Address = Envelope.select('h1#product-title')
    Stamp = Envelope.select('span.price-value')
    ReturnAddress = Envelope.select('span.currency-symbol')
    CollectorStamp = Stamp
    CountryOfOrigin = ReturnAddress
    PostKeys = Envelope.find_all('div')
    SecretMessage = ""
    while counter != enumerate(PostKeys): 
        MasterKey = Envelope.select('div')[counter]
        counter += counter
        return MasterKey
    
    Engraving = MasterKey.get_text()
    if Engraving.includes("*API*"):
        SecretMessage = Engraving

    print(f"The {Address} costs {CountryOfOrigin}{CollectorStamp}!")
    if SecretMessage != "":
        print(f"\nDon't tell the Mailman but I have their keys :) \nLook at what's engraved {SecretMessage}")

if __name__ == '__main__':
    openTheMail()    
