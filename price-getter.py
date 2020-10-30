from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup

url = "https://afropelo.com/?product_cat=hair-care"
page = urlopen(url)
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

def get_product_prices():
    products_list = soup.find_all("li", class_="product")
    prices = []
    for product in products_list:
        get_price = product.find("span",class_="woocommerce-Price-amount")
        price = get_price.text
        prices.append(price)
    print(prices)
    
if __name__ == '__main__':
    get_product_prices()



