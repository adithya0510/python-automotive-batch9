class StockAnalyzer:
    # Constructor to initialize stock prices
    def __init__(self, prices):
        self.prices = prices

    # Method to calculate maximum profit from stock prices
    def calculate_max_profit(self):
        # Minimum price initially set to the first price
        min_price = self.prices[0]
        max_profit = 0

        # Traverse prices starting from second day
        for price in self.prices[1:]:
            # Update minimum price if a lower price is found
            if price < min_price:
                min_price = price
            else:
                # Calculate profit
                profit = price - min_price
                # Update maximum profit if current profit is higher
                if profit > max_profit:
                    max_profit = profit

        return max_profit

    # Method to calculate volatility index
    def calculate_volatility_index(self):
        total_difference = 0

        # Calculate absolute difference between consecutive prices
        for i in range(1, len(self.prices)):
            total_difference += abs(self.prices[i] - self.prices[i - 1])

        # Calculate average volatility
        volatility = total_difference / (len(self.prices) - 1)
        return round(volatility, 2)


# Read stock prices from user input
prices = input().split()

# Convert string inputs to integers
prices = [int(p) for p in prices]

# Create StockAnalyzer object
analyzer = StockAnalyzer(prices)

# Display maximum profit
print(f"Max Profit: {analyzer.calculate_max_profit()}")

# Display volatility index (formatted to 2 decimals)
print(f"Volatility Index: {analyzer.calculate_volatility_index():.2f}")
