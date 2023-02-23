from bs4 import BeautifulSoup
import requests #use it to make requests from websites to grab html code
product = input('What are you searching for?: ')
product = product.replace(' ', '+')
order = input('Lowest price (ls), Best Selling (bs), Best Rated (br)?: ')
if order == 'ls':
    order = 1
elif order == 'bs':
    order = 3
else:
    order = 4
url = f'https://www.newegg.ca/p/pl?d={product}&Order={order}'

html = requests.get(url).text #gives back request object (unusable), .text converts it to text
soup = BeautifulSoup(html, 'lxml')

products = soup.find('div', class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
target = products.div
title_tag_a = target.find('a', class_='item-title')
title = title_tag_a.text
link = title_tag_a['href']

price_tag = target.find('li', class_='price-current')
price_dollar = price_tag.strong.text
price_cents = price_tag.sup.text
print()
print('Heres what youre looking for: ')
print(f'name: {title}')
print(f'price: ${price_dollar}{price_cents}')
print(f'link: {link}')