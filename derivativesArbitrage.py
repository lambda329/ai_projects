#A program to find arbitrage opportunities in derivatives contracts
import random
import time
from datetime import datetime

class Trade:
    def __init__(self, symbol, quantity, price, action):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.action = action
        self.timestamp = datetime.now()

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

    def get_price(self):
        # Mock price generation for demonstration
        return 1000 + random.uniform(-50, 50) # Random price in a range for simulation

def trading_strategy(market_data, portfolio):
    price = market_data.get_price()
    quantity = 1.0 # Define a constant trade quantity
    
    # Randomly decide to buy or sell
    action = "buy" if random.random() < 0.5 else "sell"
    if action == "buy":
        portfolio.buy(market_data.symbol, quantity, price)
    else:
        portfolio.sell(market_data.symbol, quantity, price)

def main():
    random.seed()
    
    # Initialize portfolio with starting balance
    portfolio = Portfolio(10000)
    market_data = MarketData("BTC-USD")
    
    # Simulate trading loop
    for _ in range(10):
        trading_strategy(market_data, portfolio)
        time.sleep(1) # Simulate a time interval between trades

    print("\nFinal Portfolio:")
    print(f"Balance: {portfolio.balance}")
    print("Positions:", portfolio.positions)

if __name__ == "__main__":
    main()

