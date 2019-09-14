# Stock Price Predictor
Stock Price Predictor uses a machine learning model to make predictions about future stock prices based on the historical values of those stocks.
# How does it work?
The program takes in two inputs, one for the ticker (symbol) of the stock and one for how far forward into the future the user wants the program to make predictions about the stock. Once it has this information, it creates a dataframe and uses a linear regression model to make predictions up to the timeframe specified by the user. The linear regression model graphs the data and creates a line of best fit for all of the data points and uses this line as the basis to make predictions moving further and further forward. It works particularly well for stock prices as for many stocks, the prices tend to go in one direction (up or down) over the time of their existence and so, a line that can fit right through these points results in a very high accuracy score; in the testing of this program, the typical accuracy was always above 90% and went as high as 99.96% when it was tasked with making a prediction about the stock price the very next day.
# Should I make investments using this?
While this program does a great job of making predictions based on past prices and trends, it does not take into account events going on in the real world, or even things that may be going on within the company on a given day. As such, it is entirely possible that it predicts the price of a stock to increase the next day when in reality, an event occurs that drastically makes the price drop. As such events cannot yet be taken into account, it is not adviseable as of yet to use this program to base real investments off.

Having said this, it is absolutely recommended that you compare the predictions made by this program with the real world price regularly to see the variance between the two to see to what degree the accuracy score reported by the program actually holds true. This would be a very interesting discussion point!
# Installation
1. Download and install the latest version of <a href='https://www.python.org/downloads/'>Python</a> if you do not already have it installed
2. Open up your Command Terminal (as Administrator on Windows) and enter <code>pip install pandas</code> and repeat this step three times, replacing <code>pandas</code> with <code>sklearn</code>, <code>numpy</code> and <code>yfinance</code>
3. Clone the project repository
4. <code>cd</code> into the project directory
5. Enter <code>python stock_price_predictor.py</code> to initialize the program
# Dependencies
<a href='https://pandas.pydata.org/'>Pandas</a>

<a href='https://scikit-learn.org/stable/'>scikit-learn</a>

<a href='https://numpy.org/'>NumPy</a>

<a href='https://pypi.org/project/yfinance/'>yfinance</a>
