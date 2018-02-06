import pandas as pd
import matplotlib.pyplot as plt
from Feeders.datafeeder import DataFeeder
from bittrex import Bittrex, API_V2_0, TICKINTERVAL_FIVEMIN
# In order to get the ticks, we have to use V2 API

my_Bittrex_v2 = Bittrex(None, None, api_version=API_V2_0)
my_Bittrex_v1 = Bittrex(None,None)
#Initialize bittrex object.

class BittrexFeeder(DataFeeder):
    
    def __init__(self,MarketName,interval):
        

        super().__init__()
        # dict_markets= my_Bittrex_v1.get_markets()
        # markets = dict_markets['result']
        # df_markets = pd.DataFrame(markets)                Obtain the markets name for multiple selction 
        # market_names = df_markets['MarketName']
        self.MarketName = MarketName
        self.interval = interval
        self.name = "Bittrex"
        setattr(self,"Name",self.name)

    def get_ticks(self):
        """Get DTOHLCV data from a specific market

        :param market: Specific market from Bittrex
            Example: "BTC-ETH"
        :type market: pandas.DataFrame

        :param interval: Time interval for DTOHLVC data
        :type interval : Str.

        
        :returns: pd.DataFrame

        >>> bittrex=BittrexFeeder()
        >>> bittrex.get_ticks('BTC-ETH','fiveMin)

                                         BV        C          H         L         O        V
            T
            2018-01-14 22:50:00   26.558818  0.099100  0.099330  0.098800  0.098998  268.215904

        """
        dict_ticks = my_Bittrex_v2.get_candles(
        market=self.MarketName, tick_interval=self.interval)

        dict_dtohlcv = dict_ticks['result']

        df_DTOHLCV = pd.DataFrame(dict_dtohlcv)
        df_DTOHLCV = df_DTOHLCV.set_index('T')
        df_DTOHLCV.index = pd.to_datetime(df_DTOHLCV.index)
        #Converting index type from str to datetimeindex
        return df_DTOHLCV

    def get_latest_tick(self,market,interval):
        pass


