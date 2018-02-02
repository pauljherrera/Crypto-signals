import pandas as pd
import matplotlib.pyplot as plt
from Feeders.datafeeder import DataFeeder
from bittrex import Bittrex, API_V2_0, TICKINTERVAL_FIVEMIN
# In order to get the ticks, we have to use V2 API

my_Bittrex_v2 = Bittrex(None, None, api_version=API_V2_0)
my_Bittrex_v1 = Bittrex(None,None)
#Initialize bittrex object.

class BittrexFeeder(DataFeeder):
    
    def __init__(self):
        

        super().__init__()
        dict_markets= my_Bittrex_v1.get_markets()
        markets = dict_markets['result']
        df_markets = pd.DataFrame(markets)
        market_names = df_markets['MarketName']
        setattr(self,"Markets",market_names)

    def get_ticks(self,market,interval):

        dict_ticks = my_Bittrex_v2.get_candles(
        market=market, tick_interval=interval)

        dict_dtohlcv = dict_ticks['result']

        df_DTOHLCV = pd.DataFrame(dict_dtohlcv)
        df_DTOHLCV = df_DTOHLCV.set_index('T')
        df_DTOHLCV.index = pd.to_datetime(df_DTOHLCV.index)

        return df_DTOHLCV



