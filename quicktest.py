import pandas as pd
import numpy as np
from Feeders.bittrexFeeder import BittrexFeeder
from strategy import Strategy
import matplotlib.pyplot as plt
import time
from tqdm import tqdm


def main():
    
    my_bittrex = BittrexFeeder('fiveMin')
    # Initialize BittrexFeeder
    feeder = my_bittrex.Name
    # Set Feeder name

    # Create the strategy with options from the user.
    my_strategy = Strategy(feeder, slowEMA=5,
                           fastEMA=20, window=30, threshold=10)

    
    market_list = ['BTC-LTC','BTC-ETH','BTC-XMR','BTC-CLOAK','BTC-VRC','BTC-AUR','BTC-PTC','BTC-CURE','BTC-DASH']
    markets = my_bittrex._get_markets(market_list)
    print(markets)

    while True :

        start_time = time.time()

        for market in tqdm(markets):
                    
                
            df_market = my_bittrex.get_ticks(market)

            my_strategy.Opportunity(df_market,market)
              
        time.sleep(301-((time.time() - start_time) % 60))    
        print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':

    main()
