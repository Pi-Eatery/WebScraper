import lxml
# import requests
from bs4 import BeautifulSoup

Goodies = open('/home/apple/example.html') # 'https://g.co/gemini/share/70f1dfad0518'

Envelope = BeautifulSoup(
    Goodies, 
    features='lxml'
)

 # Mail = Envelope.find('h1')

def openTheMail():
    Letter = Envelope.select('#product-title')
    print(Letter)

if __name__ == '__main__':
    openTheMail()    
