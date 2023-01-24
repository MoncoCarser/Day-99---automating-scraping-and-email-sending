import requests
from bs4 import BeautifulSoup

URL = "https://replit.com/community-hub"

response = requests.get(URL)
html = response.text
print(html)