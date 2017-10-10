#Written for python 2
#does not work with python 3.6
#If using python3.6 change import lib to urllib and update bs4 with one compatible with python3

import urllib2
from bs4 import BeautifulSoup

sStockName = raw_input("Enter the name of the stock: ")
urlPage = "http://www.nasdaq.com/symbol/%s" % sStockName

page = urllib2.urlopen(urlPage)
soup = BeautifulSoup(page, 'html.parser')

priceDivTag = soup.find(id="qwidget_lastsale")
priceValue = priceDivTag.text.strip("<div class=\"qwidget-dollar\" id=\"qwidget_lastsale\">")

print (priceValue)