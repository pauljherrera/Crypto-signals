import pandas as pd
import matplotlib.pyplot as plt
from Feeders.datafeeder import DataFeeder
from bittrex import Bittrex, API_V2_0, TICKINTERVAL_FIVEMIN
from tqdm import tqdm
import os
# In order to get the ticks, we have to use V2 API

my_Bittrex_v2 = Bittrex(None, None, api_version=API_V2_0)
my_Bittrex_v1 = Bittrex(None, None)
# Initialize bittrex object.


class BittrexFeeder(DataFeeder):

    def __init__(self, interval):

        super().__init__()
        self.interval = interval
        self.name = "Bittrex"
        setattr(self, "Name", self.name)

    def get_ticks(self, MarketName):
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
            market=MarketName, tick_interval=self.interval)

        try:
            dict_dtohlcv = dict_ticks['result']

            df_DTOHLCV = pd.DataFrame(dict_dtohlcv)

            df_DTOHLCV = df_DTOHLCV.set_index('T')

            df_DTOHLCV.index = pd.to_datetime(df_DTOHLCV.index)
        # Converting index type from str to datetimeindex
        
        except KeyError as e:
            print(e)


        return df_DTOHLCV

    def _get_latest_tick(self, MarketName):

        dict_latest_tick = my_Bittrex_v2.get_latest_candle(
            market=MarketName, tick_interval=self.interval)
        dict_dtohlcv_latest = dict_latest_tick['result']

        df_DTOHLCV_latest = pd.DataFrame(dict_dtohlcv_latest)
       
        df_DTOHLCV_latest = df_DTOHLCV_latest.set_index('T')

        df_DTOHLCV_latest.index = pd.to_datetime(df_DTOHLCV_latest.index)

        return df_DTOHLCV_latest

    def _get_markets(self,market_list = None):
      
        if market_list is not None:
            market_names = market_list
        else:
            dict_markets = my_Bittrex_v1.get_markets()
            markets = dict_markets['result']

            # Obtain the markets name for multiple selection
            df_markets = pd.DataFrame(markets)

            market_names = df_markets['MarketName']


        
        return market_names

    def historical_data(self):
        market_dict = {}
        markets = self._get_markets()
        #markets = ['BTC-ETH']
        for market in tqdm(markets):
            try:
                market_dict[market] = self.get_ticks(market)
            except KeyError as identifier:
                print("/n Error")
                os.system('cls')

        return(market_dict)

    def append_latest_tick(self,DataFrame,MarketName):

        new_tick = self._get_latest_tick(MarketName)
        historical_ticks = DataFrame

        new_data = historical_ticks.append(new_tick)

        return new_data

        