import lxml
# import requests
from bs4 import BeautifulSoup

with open('/home/apple/example.html') as Goodies

Envelope = BeautifulSoup(
    Goodies, 
    'html.parser'
)

 # Mail = Envelope.find('h1')

def openTheMail():
    Letter = Envelope.select('span.price-value')
    print(Letter)
    Words = Letter

if __name__ == '__main__':
    openTheMail()    
