from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests

session = HTMLSession()
resp= session.get("https://grocery.walmart.com/browse/Milk?aisle=1255027787061_1255027788656")
resp.html.render()
resp.html.html
soup = BeautifulSoup(resp.html.html, "lxml")
# productTiles=soup.find_all('div',{'data-automation-id':'productTile'})
productTiles=soup.find_all('div',{'data-automation-id':'productTile'})
for productTile in productTiles:
    print(productTile.attrs['aria-label'])
    print(productTile.find(attrs={"data-automation-id": "price"}).span.string)
