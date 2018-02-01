import pandas as pd
import matplotlib.pyplot as plt
from datafeeder import DataFeeder
from bittrex import Bittrex, API_V2_0, TICKINTERVAL_FIVEMIN
# In order to get the ticks, we have to use V2 API

my_Bittrex = Bittrex(None, None, api_version=API_V2_0)




test = ticks_dict['result']

df = pd.DataFrame(test)
df2 = df.set_index('T')
df2.index = pd.to_datetime(df2.index)
print(type(df2.index))

class BittrexFeeder(DataFeeder):
    
    def __init__(self,Coins):
        

        super().__init__()

        data = coins
        setattr(self,"Coins",data)

    def get_ticks(self,market,interval):

        ticks_dict = my_Bittrex.get_candles(
        market="BTC-ETH", tick_interval=TICKINTERVAL_FIVEMIN)
