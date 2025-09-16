import lxml
import requests
from bs4 import BeautifulSoup

Goodies = 'https://g.co/gemini/share/70f1dfad0518'
Delivery = requests.get(Goodies)
Envelope = BeautifulSoup(Delivery, features='lxml')
Mail = Envelope.find()
openTheMail = print(Mail)

if __name__ == '__main__':
    openTheMail
    
