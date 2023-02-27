"""
Name: Jacob Piskadlo
Date: 2/20/2023
Project: Stock Evaluator
Class Name: dataProcessor
Description: Class to collect data from a web scraper and interpret it using a linear regression
"""
import numpy as np
from sklearn.linear_model import LinearRegression
from webScraper import webScraper
import time


'''
Class to take in data from webscraper, and run linear regression algorithm
'''
class dataProcessor:

	def __init__(self):
		self.data = []
		self.num = []
		self.ws = webScraper()


	'''
	Parameters: tm - int representing time interval | tick - string representation of ticker symbol
	Returns: None
	Description: Using the webScraper, loads in 10 data points to be run with a linear regression
	'''
	def load_data(self, tm, tick):
		page = self.ws.establish_connection(tick)
		for i in range(1, 11):
			self.num.append(i)
			self.data.append(float(self.ws.find_element(page)))
			print("Loading...")
			time.sleep(tm)



	'''
	Parameters: None
	Returns: int representing the result of the linear regression
	Description: Using loaded data, runs a linear regression and returns next predicted stock price.
	'''
	def lin_reg(self):
		self.num = np.reshape(self.num,(-1, 1))
		model = LinearRegression()
		model.fit(self.num,self.data)
		predictors = [11]
		return model.predict(np.reshape(predictors,(-1,1)))


