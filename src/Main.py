"""
Name: Jacob Piskadlo
Date: 2/20/2023
Project: Stock Evaluator
Class Name: Main()
Description: Main program to run a web scraper and data processing unit.
This will be used to run a linear regression algorithm to predict the next possible price of a stock
"""
from dataProcessor import dataProcessor

'''
Main Program to run a linear regression algorithm on stock prices to predict next price
'''
class Main():

	def __init__(self):
		self.dp = dataProcessor()
		self.time = self.get_time()
		self.tick = self.get_ticker()
		self.run()

	'''
	Parameters: None
	Returns: None
	Description: Runs main program returning predicted stock price
	'''
	def run(self):
		self.dp.load_data(self.time, self.tick)
		num = round(float(self.dp.lin_reg()), 2)
		print("Next Stock Price is ", num)

	'''
	Parameters: None
	Returns: Int representing time interval
	Description: Gets time interval from user
	'''
	def get_time(self):
		time_int = input("Enter desired time interval (seconds): ")
		return int(time_int)

	'''
	Parameters: None
	Returns: String representing ticker symbol
	Description: Gets ticker symbol from user
	'''
	def get_ticker(self):
		tick = input("Enter ticker symbol: ")
		return tick.upper()




Main()
