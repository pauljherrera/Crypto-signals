import pandas as pd
import matplotlib.pyplot as plt
from datafeeder import DataFeeder
from bittrex import Bittrex, API_V2_0, TICKINTERVAL_FIVEMIN
# In order to get the ticks, we have to use V2 API

my_Bittrex = Bittrex(None, None, api_version=API_V2_0)
#Initialize bittrex object.

class BittrexFeeder(DataFeeder):
    
    def __init__(self,coins):
        

        super().__init__()

        data = coins
        setattr(self,"Coins",data)

    def get_ticks(self,market,interval):

        dict_ticks = my_Bittrex.get_candles(
        market=market, tick_interval=interval)

        dict_dtohlcv = dict_ticks['result']

        df_DTOHLCV = pd.DataFrame(dict_dtohlcv)
        df_DTOHLCV = df_DTOHLCV.set_index('T')
        df_DTOHLCV.index = pd.to_datetime(df_DTOHLCV.index)

        return df_DTOHLCV

