import pandas as pd 
import numpy as np
from Feeders.bittrexFeeder import BittrexFeeder
import matplotlib.pyplot as plt


def ExpMovingAverage(values, window):
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    a =  np.convolve(values, weights, mode='full')[:len(values)]
    a[:window] = a[window]
    colum_name = 'ema ' + str(window)
    df_a = pd.DataFrame(a,columns=[colum_name])
    return df_a

my_bittrex = BittrexFeeder()

try:
    dtohlcv = my_bittrex.get_ticks('BTC-ETH','day')
except KeyError :
    pass

    
    
close_values = my_bittrex.get_close(dtohlcv)
a = pd.DataFrame(close_values)
emaslow = ExpMovingAverage(close_values,5)
emafast = ExpMovingAverage(close_values,20)
emaslow.index = close_values.index
emafast.index = close_values.index
CN=pd.concat([a,emaslow,emafast],axis=1)

CN.plot()

plt.show()
