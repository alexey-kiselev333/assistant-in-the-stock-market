import yfinance as yf

# Get the data for the stock AAPL
data = yf.download('AAPL','2016-01-01','2021-02-03')

# Import the plotting library
import matplotlib.pyplot as plt


# Plot the close price of the AAPL
data['Adj Close'].plot()
plt.show()