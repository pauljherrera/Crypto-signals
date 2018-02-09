import pandas as pd
import numpy as np
from Feeders.bittrexFeeder import BittrexFeeder
from strategy import Strategy
import matplotlib.pyplot as plt
import time
from tqdm import tqdm


def main():
    
    my_bittrex = BittrexFeeder()
    # Initialize BittrexFeeder
    feeder = my_bittrex.name
    # Set Feeder name

    # Create the strategy with options from the user.
    my_strategy = Strategy(feeder)

    markets = my_bittrex._get_markets()
    print(markets)

    while True :

        start_time1 = time.time()

        for market in tqdm(markets):
                    
            start_time = time.time()    
            df_market = my_bittrex.get_ticks(market)
            tqdm.write("--- %s seconds ---" % (time.time() - start_time))
            status = my_strategy.Opportunity(df_market,market)
            tqdm.write(str(status))
              
        #time.sleep(301-((time.time() - start_time) % 60))    
        print("--- %s seconds ---" % (time.time() - start_time1))


if __name__ == '__main__':

    main()
