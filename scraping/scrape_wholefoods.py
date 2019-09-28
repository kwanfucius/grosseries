from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests

session = HTMLSession()
resp= session.get("https://products.wholefoodsmarket.com/search?sort=relevance&store=10041&text=milk")
resp.html.render()
print(resp.html.html)
soup = BeautifulSoup(resp.html.html, "lxml")
# productTiles=soup.find_all('div',{'data-automation-id':'productTile'})
productTiles=soup.find_all('div',{'data-automation-id':'productTile'})
# for productTile in productTiles:
#     print(productTile.attrs['aria-label'])
#     print(productTile.find(attrs={"data-automation-id": "price"}).span.string)
