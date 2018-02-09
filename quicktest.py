import pandas as pd
import numpy as np
from Feeders.bittrexFeeder import BittrexFeeder
from strategy import Strategy
import matplotlib.pyplot as plt
from datetime import datetime
import time
from tqdm import tqdm
from config import bittrex_config

from apscheduler.schedulers.blocking import BlockingScheduler
import threading


# Initializing components.

my_bittrex = BittrexFeeder()
feeder = my_bittrex.name
my_strategy = Strategy(feeder)

def analyze_market(market):
    global my_bittrex
    global my_strategy

    df_market = my_bittrex.get_ticks(market)
    my_strategy.Opportunity(df_market, market)

    print("\n{} analyzed succesfully.".format(market))


def run(markets):
    print("\nRetrieving data from the exchanges...\n")
    for market in markets:
        thread = threading.Thread(target=analyze_market, args=[market])
        thread.start()

    print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])



def main():
    global my_bittrex
    global my_strategy

    # Create the strategy with options from the user.
    print("\nApp started. Monitoring the following pairs:")

    markets = my_bittrex._get_markets()
    print(markets)

    scheduler = BlockingScheduler()
    scheduler.add_job(run, trigger='cron', minute='*/2', args=[markets])
    scheduler.start()


if __name__ == '__main__':

    main()
