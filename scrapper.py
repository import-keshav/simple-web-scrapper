from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

my_url = input("Please enter a link from rokomari.com: \n")

client = req(my_url)
page_html = client.read()
client.close()

page_soup = soup(page_html, 'html.parser')

containers = page_soup.find_all('div', {'class': 'bookListItem'})

filename = 'scrapped_book.csv'
f = open(filename, 'w')
header = 'book name, price, author, image\n'
f.write(header)

for container in containers:
    name = container.img['alt']
    image = container.img['data-src']
    price = container.p.find('span', {'class': 'presentPrice'}).text
    author = container.ul.li.span.text

    f.write(name.replace(',', '') + ',' + price.replace(',', '') + ',' + author + ',' + image + '\n')

f.close()
