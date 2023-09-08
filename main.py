import yfinance as yf

meta_data = yf.download('META', period='1y')

# Save the data to csv file
meta_data.to_csv('meta_stock_data.csv')
