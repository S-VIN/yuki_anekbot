import time

import requests
from bs4 import BeautifulSoup
from db import db

url = 'https://baneks.ru/'

import re

def get_anekdot(url):
    response = requests.get(url)
    response.raise_for_status()

    match = re.search(r'<meta property="og:description" content="(.*?)"/>', response.text, re.DOTALL)
    if match:
        return match.group(1)
    else:
        raise Exception('Анекдот не найден!')



for i in range(1, 1142):
    time.sleep(0.1)
    anek = get_anekdot(url + str(i))
    if anek and anek != '':
        print(i, anek)
        print()
        print()
        db.add_anek_sync(anek)

