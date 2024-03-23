import yfinance as yf

# ticker = yf.Ticker('AAPL')
# stock_info = ticker.fast_info
# stock_info.keys()

# Replace 'AAPL' with the ticker symbol of the company you're interested in
ticker = 'AAPL'
stock = yf.Ticker(ticker)

# Get balance sheet data
balance_sheet = stock.balance_sheet
data_top_balance_sheet = balance_sheet.head()
# print(data_top_balance_sheet)

financials = stock.financials
data_top_financials = financials.head()
# print(data_top_financials)

financialData = stock.financialData
data_top_financialData = financialData.head()
print(data_top_financialData)


# # Extract total liabilities and total equity
# total_liabilities = balance_sheet.loc['Total Liab'][0]
# total_equity = balance_sheet.loc['Total Stockholder Equity'][0]

# # Calculate the Debt-to-Equity Ratio
# de_ratio = total_liabilities / total_equity
# print(f"The Debt-to-Equity Ratio for {ticker} is: {de_ratio:.2f}")

###############

# operation margin

# Replace 'AAPL' with the ticker symbol of the company you're interested in
ticker_symbol = 'AAPL'

# Fetch the company's data
company = yf.Ticker(ticker_symbol)

# Fetch the income statement
income_statement = company.financials

# Extract operating income and revenue
operating_income = income_statement.loc['Operating Income',:].iloc[0]  # Most recent year
revenue = income_statement.loc['Total Revenue',:].iloc[0]  # Most recent year

# Calculate operating margin
operating_margin = (operating_income / revenue) * 100

print(f"The Operating Margin for {ticker_symbol} is: {operating_margin:.2f}%")

###############

# Replace 'AAPL' with the ticker of the company you're interested in
ticker_symbol = 'AAPL'

# Fetch the company data
company = yf.Ticker(ticker_symbol)

# Fetch the annual financials
financials = company.financials
balance_sheet = company.balance_sheet

print(balance_sheet.head)

# Net Income (from the last annual financials)
net_income = financials.loc['Net Income'].iloc[0]

# Shareholder Equity (from the last annual balance sheet)
shareholder_equity = balance_sheet.loc['Total Stockholder Equity'].iloc[0]

# Calculate ROE
roe = (net_income / shareholder_equity) * 100  # Convert to percentage

print(f"Return on Equity (ROE) for {ticker_symbol}: {roe:.2f}%")
