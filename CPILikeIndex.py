"""Traditional Consumer Price Index (CPI) measures track changes over time in the price 
level of a market basket of consumer goods and services purchased by households, but they 
are usually published on a monthly or quarterly basis, which might not capture rapid 
market changes.

Therefore, using commodities spot price to manually construct a CPI-like index is an approach 
to gauge the market's current situation more dynamically

***Categories to Consider***

Energy: Oil (Brent, WTI), Natural Gas, Coal. These are essential for transportation, heating, 
    and electricity generation.
Metals: Gold, Silver, Copper, Aluminum. These are indicators of industrial activity and consumer 
    demand for durable goods.
Agricultural: Wheat, Corn, Soybeans, Rice, Cotton. Food and clothing commodities affect consumer 
    budgets significantly.
Livestock: Live Cattle, Lean Hogs. Prices impact the cost of meat, affecting food inflation.


***Calculating the CPI-like Index***
Determine the Base Period - Select a base period for our index, which will serve as the point of 
    comparison for future prices.
Calculate the Price Relative - For each commodity, calculate the price relative, which is the 
    ratio of the current spot price to the base period price.
Assign Weights - Assign weights to each commodity based on its importance in the average consumer's 
    expenditure. This might require some research or assumptions based on available market data
     - Aggregate the Index Multiply the price relative of each commodity by its weight, and then 
    sum these values to get the overall index.

Formula:
CPI-like Index = sum(Price_Relative_i times Weight_i)

Where i represents each commodity in our basket.

***Sources for Commodities Spot Live Prices***

Financial News Websites: Bloomberg, Reuters, and CNBC offer real-time data and news on commodity 
    markets.
Market Data Providers: Services like TradingView, Investopedia, and MarketWatch provide live spot 
    prices for a range of commodities.
Commodity Exchanges: Websites of major commodity exchanges (e.g., NYMEX for energy commodities, 
    CBOT for agricultural commodities) often have the most up-to-date prices.
"""

class CPILikeIndex:
    def __init__(self):
        self.base_prices = {'Energy': {}, 'Metals': {}, 'Agricultural': {}, 'Livestock': {}}
        self.current_prices = {'Energy': {}, 'Metals': {}, 'Agricultural': {}, 'Livestock': {}}
        self.weights = {'Energy': {}, 'Metals': {}, 'Agricultural': {}, 'Livestock': {}}

    def set_base_prices(self, category, prices):
        """
        Set base prices for a category of commodities.
        
        :param category: The category of commodities (Energy, Metals, etc.)
        :param prices: A dictionary of commodities and their base prices
        """
        if category in self.base_prices:
            self.base_prices[category].update(prices)
        else:
            print(f"Category '{category}' not recognized.")

    def update_current_prices(self, category, prices):
        """
        Update current spot prices for a category of commodities.
        
        :param category: The category of commodities (Energy, Metals, etc.)
        :param prices: A dictionary of commodities and their current prices
        """
        if category in self.current_prices:
            self.current_prices[category].update(prices)
        else:
            print(f"Category '{category}' not recognized.")

    def assign_weights(self, category, weights):
        """
        Assign weights to commodities within a category.
        
        :param category: The category of commodities (Energy, Metals, etc.)
        :param weights: A dictionary of commodities and their weights
        """
        if category in self.weights:
            self.weights[category].update(weights)
        else:
            print(f"Category '{category}' not recognized.")

    def calculate_price_relative(self, category, commodity):
        """
        Calculate the price relative for a commodity.
        
        :param category: The category of the commodity
        :param commodity: The name of the commodity
        :return: The price relative of the commodity or None if data is missing
        """
        try:
            base_price = self.base_prices[category][commodity]
            current_price = self.current_prices[category][commodity]
            return current_price / base_price
        except KeyError:
            print(f"Data for '{commodity}' in category '{category}' is incomplete.")
            return None

    def calculate_index(self):
        """
        Calculate the overall CPI-like index based on current prices and weights.
        
        :return: The calculated CPI-like index
        """
        index = 0
        for category in self.weights.keys():
            for commodity, weight in self.weights[category].items():
                price_relative = self.calculate_price_relative(category, commodity)
                if price_relative is not None:
                    index += price_relative * weight
        return index

# Example usage:
# index_calculator = CPILikeIndex()
# index_calculator.set_base_prices('Energy', {'Oil (Brent)': 60, 'Natural Gas': 2.5})
# index_calculator.update_current_prices('Energy', {'Oil (Brent)': 70, 'Natural Gas': 3})
# index_calculator.assign_weights('Energy', {'Oil (Brent)': 0.5, 'Natural Gas': 0.5})
# print(index_calculator.calculate_index())