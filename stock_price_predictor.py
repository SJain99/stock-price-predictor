import pandas as pd
import yfinance as yf
import math
import numpy as np
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = None
decimal = None

# Takes in a ticker input and if the ticker is real, creates a dataframe with the information of that stock
def stock_checker():
	global df
	ticker_input = input('Enter the ticker of the stock you want to predict the price of (ex. Google = GOOGL): ')
	print('\n')
	try:
		ticker = yf.Ticker(ticker_input)
		df = ticker.history(period='max')
	except ValueError:
		print('There was no file found with that input. Please try again.')
		stock_checker()
	ticker_input = ticker_input.upper()
	stock_checker.ticker_input = ticker_input

# Determines the decimal that will be used to determine the timeframe into the future that the model will make predictions for
def days_into_future():
	global df, decimal
	try:
		num_days = int(input('How many days into the future would you like to predict the price for? Pick a number between 1 and 730. '))
		if num_days <= 0 or num_days > 730:
			raise ValueError
	except ValueError:
		print('There was an error with your input. Please try again.')
		days_into_future()
	print('\n')
	decimal = 1/(len(df)/num_days)

# Initializes the program
if __name__ == '__main__':
	print('Welcome to the Stock Price Predictor. This program uses a linear regression machine learning model to predict the price of a stock between a ' + 
		  'period of 1 day and 2 years into the future. To do this, it analyzes the historical price data of the stock and creates a line of best fit ' + 
		  'to this data to make the predictions leading forward.\n\nNOTE: This program does not take into account things that are currently happening ' + 
		  'in the real world and so, the predictions that are made are never going to be totally accurate, even if the accuracy percentage is high. ' + 
		  'Please be careful if you base investments into stocks based on this program. The creator takes no responsibility for losses that may be ' + 
		  'incurred as a result of using this program.\n')
	stock_checker()
	days_into_future()

	# Eliminates unnecessary columns in the dataframe and temporarily fills empty (NaN) cells in the dataframe
	df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
	df.fillna(-100000, inplace = True)

	# Determines the prediction timeframe and creates a new column in the dataframe where all the values in the 'Close' column are shifted up
	# by a factor of 'future_forecast' rows
	future_forecast = int(math.ceil(decimal*len(df)))
	df['Label'] = df['Close'].shift(-future_forecast)

	# Creates an array of values found in the dataframe but excludes the 'Label' column
	X = np.array(df.drop(['Label'], axis = 1))

	# Sets 'X' dataframe equal to historical data and 'recent_X' equal to the most recent data by a factor of 'future_forecast'
	X = X[:-future_forecast]
	recent_X = X[-future_forecast:]

	# Removes the empty cells from the dataframe
	df.dropna(inplace = True)

	# Creates a array with just the 'Label' column from 'df'
	y = np.array(df['Label'])

	# Splits the data into training and testing sets
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

	# Creates the linear regression model and fits the training sets into it
	model = LinearRegression()
	model.fit(X_train, y_train)

	# Determines the accuracy score given the testing sets
	accuracy = model.score(X_test, y_test)

	# Makes relevant predictions for the specified timeframe using the 'recent_X' array
	predictions = model.predict(recent_X)
	
	print(f'In {future_forecast} day(s), the stock price of {stock_checker.ticker_input} will be approximately ${round(predictions[-1], 2)} USD. This result is {accuracy*100}% accurate as of {datetime.now()}.')