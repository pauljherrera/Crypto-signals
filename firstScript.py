import pandas as pd 
from bittrexFeeder import BittrexFeeder
import time
start_time = time.time()

def main():
    bittrex = BittrexFeeder()
    markets = bittrex.Markets



    a=0
    for k in markets:
       
        try:
            ohlcv = bittrex.get_ticks(k,'hour')
        except KeyError :
            pass
        finally :  
            print(k)
            print(ohlcv)
            a = a+1
            print(a)



    # ohlcv = bittrex.get_ticks("BTC-ETH","hour")

    # print(ohlcv)

    # openValue = bittrex.get_open(ohlcv)

    # print(openValue)


    # volumeValue = bittrex.get_volume(ohlcv)

    # print(volumeValue)












if __name__ == '__main__':
    main()
    print("--- %s seconds ---" % (time.time() - start_time))