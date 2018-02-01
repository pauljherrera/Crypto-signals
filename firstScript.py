import pandas as pd 
from bittrexFeeder import BittrexFeeder

def main():
    bittrex = BittrexFeeder("Hola")
    print(bittrex.Coins)

    ohlcv = bittrex.get_ticks("BTC-ETH","hour")

    print(ohlcv)

    openValue = bittrex.get_open(ohlcv)

    print(openValue)


    volumeValue = bittrex.get_volume(ohlcv)

    print(volumeValue)






















if __name__ == '__main__':
    main()
    