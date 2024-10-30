#Program to implement a basic moving average crossover trading strategy.
import random
import time
from collections import deque

class Trade:
    def __init__(self, symbol, quantity, price, action):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.action = action
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.timestamp}: {self.action.upper()} {self.quantity} of {self.symbol} at {self.price}"

class Portfolio:
    def __init__(self, balance):
        self.balance = balance
        self.positions = {}

    def buy(self, symbol, quantity, price):
        cost = quantity * price
        if self.balance >= cost:
            self.balance -= cost
            self.positions[symbol] = self.positions.get(symbol, 0) + quantity
            print(f"Bought {quantity} of {symbol} at {price}. New Balance: {self.balance}")
        else:
            print("Insufficient balance to execute buy order.")

    def sell(self, symbol, quantity, price):
        if self.positions.get(symbol, 0) >= quantity:
            self.positions[symbol] -= quantity
            self.balance += quantity * price
            print(f"Sold {quantity} of {symbol} at {price}. New Balance: {self.balance}")
        else:
            print("Insufficient holdings to execute sell order.")

class MarketData:
    def __init__(self, symbol):
        self.symbol = symbol
        self.prices = deque(maxlen=20) # Store the last 20 prices for moving average calculation

    def get_price(self):
        # Mock price generation for demonstration
        price = 1000 + random.uniform(-50, 50)
        self.prices.append(price)
        return price

    def get_moving_average(self, period):
        if len(self.prices) < period:
            return None # Not enough data for the moving average
        return sum(list(self.prices)[-period:]) / period

def moving_average_crossover_strategy(market_data, portfolio):
    price = market_data.get_price()
    short_ma = market_data.get_moving_average(5)
    long_ma = market_data.get_moving_average(20)

    # Only proceed if we have enough data for both MAs
    if short_ma is None or long_ma is None:
        return

    # Moving average crossover strategy
    quantity = 1.0 # Define trade quantity

    # Buy signal: short MA crosses above long MA
    if short_ma > long_ma and not portfolio.positions.get(market_data.symbol, 0):
        portfolio.buy(market_data.symbol, quantity, price)
        print(f"Buy signal - Price: {price}, Short MA: {short_ma}, Long MA: {long_ma}")

    # Sell signal: short MA crosses below long MA
    elif short_ma < long_ma and portfolio.positions.get(market_data.symbol, 0) > 0:
        portfolio.sell(market_data.symbol, quantity, price)
        print(f"Sell signal - Price: {price}, Short MA: {short_ma}, Long MA: {long_ma}")

def main():
    random.seed()
    
    # Initialize portfolio with starting balance
    portfolio = Portfolio(10000)
    market_data = MarketData("BTC-USD")
    
    # Simulate trading loop
    for _ in range(50):
        moving_average_crossover_strategy(market_data, portfolio)
        time.sleep(1) # Simulate a time interval between trades

    print("\nFinal Portfolio:")
    print(f"Balance: {portfolio.balance}")
    print("Positions:", portfolio.positions)

if __name__ == "__main__":
    main()
