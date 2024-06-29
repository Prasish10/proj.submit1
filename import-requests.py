import requests
from bs4 import BeautifulSoup

urls ='https://en.wikipedia.org/wiki/Nepal_Stock_Exchange'
req=requests.get(urls)

soup=BeautifulSoup(req.content,'html.parser')

titles=soup.find('span',class_='mw-page-title-main')
print(titles.get_text())

describes=soup.find('div',class_='mw-content-ltr')
for paragraph in describes.find_all('p'):
    print(paragraph.get_text())
  
 
tags = soup.find('ul')
if tags:
    print(tags.text)
else:
    print("No <ul> tag found")


# import sqlite3
# import requests
# from bs4 import BeautifulSoup

# conn = sqlite3.connect('Broker.db')
# c = conn.cursor()

# # c.execute('''CREATE TABLE IF NOT EXISTS Broker (id INTEGER PRIMARY KEY,broker no., broker, address)''')

# url = 'https://en.wikipedia.org/wiki/Nepal_Stock_Exchange'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')

# quotes = soup.find_all('span', class_='text')
# authors = soup.find_all('small', class_='author')
# tags = soup.find_all('div', class_='tags')

import pandas as pd
from sqlalchemy import create_engine

data = {
    "Broker No.": ["1", "1_RWS", "3", "4", "5", "6", "6_RWS", "6_RWS", "7", "7_RWS", "8", "8_RWS"],
    "Broker Name": [
        "Kumari Securities Pvt. Limited",
        "Kumari Securities Pvt. Limited",
        "Arun Securities Pvt. Limited",
        "Stock Broker Opal Securities Investment Pvt. Limited",
        "Market Securities Exchange Company Pvt. Limited",
        "Agrawal Securities Pvt. Limited",
        "Agrawal Securities Pvt.Limited",
        "Agrawal Securities Pvt.Limited",
        "J.F. Securities Company Pvt. Limited",
        "J.F. Securities Company Pvt. Limited",
        "Ashutosh Brokerage & Securities Pvt. Limited",
        "Ashutosh Brokerage & Securities Pvt. Limited"
    ],
    "Address": [
        "Dillibazaar, Kathmandu",
        "New Road, Pokhara",
        "Gaushala, Kathmandu",
        "Lazimpat, Kathmandu",
        "OM Dev Plaza Complex, Kichha Pokhari, Kathmandu",
        "Dillibazar, Kathmandu",
        "Main Road, Biratnagar",
        "Kadam Chowk, Janakpur",
        "New Road, Kathmandu",
        "Tulsipur, Dang",
        "Behind Nepal SBI Bank, Battisputali, Kathmandu",
        "United Insurance Building, Kathmandu"
    ]
}

df = pd.DataFrame(data)

print(df)

engine = create_engine('sqlite:///brokers.db')

df.to_sql('brokers', engine, if_exists='replace', index=False)

print("Data has been written to the database.")