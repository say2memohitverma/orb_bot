from trade_client import TradeClient
from trading import TradeORB
from log_wrapper import LogWrapper
import threading
#practice account so security threat
accountID = '101-001-19034598-001'
token = '06e811dacdba86915a05a7031c744136-94a79c4cfede80f7362248aa069e8214'


# creating oanda client object
trade_client = TradeClient(accountID, token)

# EURO USD trading object
trade_EUR_USD = TradeORB(trade_client, "EUR_USD")

# AUS CAD (Australian Dollar-Canadian Dollar) trading object
trade_AUD_CAD = TradeORB(trade_client, "AUD_CAD")

# EUR JPY trading object
trade_EUR_JPY = TradeORB(trade_client, "EUR_JPY")


def start_trading(trading_obj):
    # infinite loop over buy sell method
    while True:
        trading_obj.buy_sell_ORB()


if __name__ == '__main__':
    # creating thread for each object type
    t1 = threading.Thread(target=start_trading, args=(trade_EUR_USD,))
    t2 = threading.Thread(target=start_trading, args=(trade_AUD_CAD,))
    t3 = threading.Thread(target=start_trading, args=(trade_EUR_JPY,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    # starting thread 3
    t3.start()

    # if threads completely executed
    print("Trading BOT Running.....")






