import alpaca_trade_api as tradeapi
from config import *
from datetime import date, timedelta

class AlpacaTrader:
    def __init__(self):
        self.alpaca = tradeapi.REST(API_KEY, SECRET_KEY, APCA_API_BASE_URL, 'v2')
        self.account = self.alpaca.get_account()

        stockUniverse = ['DOMO', 'TLRY', 'SQ', 'MRO', 'AAPL', 'GM', 'SNAP', 'SHOP',
                         'SPLK', 'BA', 'AMZN', 'SUI', 'SUN', 'TSLA', 'CGC', 'SPWR',
                         'NIO', 'CAT', 'MSFT', 'PANW', 'OKTA', 'TWTR', 'TM', 'RTN',
                         'ATVI', 'GS', 'BAC', 'MS', 'TWLO', 'QCOM', ]
        # Format the allStocks variable for use in the class.
        self.allStocks = []
        for stock in stockUniverse:
            self.allStocks.append([stock, 0])

    def run(self):
        # First, cancel any existing orders so they don't impact our buying power.
        self.alpaca.cancel_all_orders()
        order = self.buy('AAPL', 3)
        print("Order Status:", order)

    """
    Checks whether there are sufficient funds to buy at input price
    """
    def checkBuy(self, symbol, shares):
        if self.account.trading_blocked:
            print("Account is currently restricted from trading")
            return False

        return True

    def buy(self, symbol, shares):
        if self.checkBuy(symbol, shares):
            self.alpaca.submit_order(
                symbol=symbol,
                qty=shares,
                side="buy",
                type="market",
                time_in_force="day",
            )
            return True

        else:
            print(f"The buy limit could not be set for {shares} shares of {symbol}")
            return False




#Delete this stuff
    # Run the LongShort class
trader = AlpacaTrader()
trader.run()