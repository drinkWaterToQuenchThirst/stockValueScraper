import urllib2
from bs4 import BeautifulSoup

urlPage = 'http://www.nasdaq.com/symbol/aapl'

page = urllib2.urlopen(urlPage)

soup = BeautifulSoup(page, 'html.parser')

priceDivTag = soup.find(id="qwidget_lastsale")

print priceDivTag

#name = name_box.text.strip()