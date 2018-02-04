import pandas as pd 
import numpy as np


class EMACrossoverBullish(object):
    def __init__(self, data, slowEMA, fastEMA):
        self.slowEMA = slowEMA
        self.fastEMA = fastEMA 
        self.data = data


    def _ExpMovingAverage(self,values, window):
        weights = np.exp(np.linspace(-1., 0., window))
        weights /= weights.sum()
        a =  np.convolve(values, weights, mode='full')[:len(values)]
        a[:window] = a[window]
        
        return a

    def Crossover (self):
        data = self.data
        data['slowEma'] = self._ExpMovingAverage(data['C'],self.slowEMA)
        data['fastEma'] = self._ExpMovingAverage(data['C'],self.fastEMA)
        data['Crossover'] = np.where(data['slowEma']>data['fastEma'],1,0)
        return data