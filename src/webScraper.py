"""
Name: Jacob Piskadlo
Date: 2/20/2023
Project: Stock Evaluator
Class Name: webScraper
Description: Class to web scrape stock prices from yahoo finance.
Will then be reported back to a data processor
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

'''
Class to establish connection and scrape stock prices from yahoo finance
'''
class webScraper:

	def __init__(self):
		pass



	'''
	Parameters: tick - string representing ticker symbol
	Returns: page - webpage to be scraped
	Description: Function to establish connection with the website to be scraped
	'''
	def establish_connection(self, tick):
		URL = "https://finance.yahoo.com/quote/{ticker}/".format(ticker = tick)
		response = requests.get(URL)
		if not response.ok:
			print('Status code:', response.status_code)
			raise Exception("Page Failed to Load")
		txt = response.text
		page = BeautifulSoup(txt, 'html.parser')
		return page

	'''
	Parameters: pg - page representing website to be scraped
	Returns: string - represents the current stock price
	Description: Function to web scrape stock price from the website
	'''
	def find_element(self, pg):
		page = pg
		a_tags = page.find_all("fin-streamer", class_="Fw(b) Fz(36px) Mb(-4px) D(ib)")
		for tag in a_tags:
			return tag.text