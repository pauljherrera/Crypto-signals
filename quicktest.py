import pandas as pd
import numpy as np
from Feeders.bittrexFeeder import BittrexFeeder
from strategy import Strategy
import matplotlib.pyplot as plt
import time
start_time = time.time()


def main():
    while True:
        
        dtohlcv = my_bittrex.get_ticks()
        #Get data ticks from bittrex
        my_strategy = Strategy(feeder, data=dtohlcv, slowEMA=5,
                           fastEMA=20, window=30, threshold=10)
        print(my_strategy.Opportunity())
        #plt.show()
        time.sleep(315)
        

if __name__ == '__main__':

    my_bittrex = BittrexFeeder('BTC-ETH', 'fiveMin')
    #Initialize BittrexFeeder
    feeder = my_bittrex.Name
    #Set Feeder name
   
    #Create the strategy with options from the user.

    main()
