#!/usr/bin/env python

"""
Written for python 2
does not work with python 3.6
If using python3.6 change import lib to urllib and update bs4 with one compatible with python3
"""


import urllib2
from bs4 import BeautifulSoup

def removeTags(parsedString, textToStrip):
	 finalValue = parsedString.text.strip(textToStrip)
	 return finalValue

def parsePage(pageURL, parsedLine):

	page = urllib2.urlopen(pageURL)
	soup = BeautifulSoup(page, 'html.parser')
	parsedString = soup.find(id="qwidget_lastsale")
	return parsedString

def main():

	sStockName = raw_input("Enter the name of the stock: ")
	urlPage = "http://www.nasdaq.com/symbol/%s" % sStockName
	
	parsedLine = "aed"
	#parsedLine = "id=\"qwidget_lastsale\""
	textToStrip = "<div class=\"qwidget-dollar\" id=\"qwidget_lastsale\">"
	
	finalString = removeTags(parsePage(urlPage, parsedLine), textToStrip)
	print(finalString)

if __name__ == "__main__":
	main()



"""
import urllib2
from bs4 import BeautifulSoup





priceDivTag = soup.find(id="qwidget_lastsale")
priceValue = priceDivTag.text.strip("<div class=\"qwidget-dollar\" id=\"qwidget_lastsale\">")

print (priceValue)
"""