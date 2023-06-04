import requests
import csv
from bs4 import BeautifulSoup
from time import sleep
from random import randint

payloads = {'pagenumber': 1}
url = 'https://nova.ge/sayofackhovrebo-da-dekoracia'
h = {'Accept-Language': 'en-US'}
response = requests.get(url, params=payloads, headers=h)
content = response.text
# print(response)
soup = BeautifulSoup(content, 'html.parser')
file = open('items.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['title', 'price'])

while payloads['pagenumber'] < 160:
    response = requests.get(url, params=payloads, headers=h)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    item_soup = soup.find('section', class_='results__container')
    all_items = item_soup.find_all('div', class_='category__result--item')
    for item in all_items:
        title = item.h3.text
        price = item.find('span', class_='product__item--price').text
        print(title, price)
        csv_obj.writerow([title, price])
        payloads['pagenumber'] += 1
        sleep(randint(1, 10))

file.close()
