# Required : pip install request bs4
import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.mitre10.co.nz/shop/dewalt-flexvolt-combo-kit-2-piece-18-volt-6-0ah/p/327395'

headers = {"User_Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

