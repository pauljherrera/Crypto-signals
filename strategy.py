import pandas as pd 
import numpy as np


class Strategy(object):
    """This class indicates an investment opportunity 
    """


    def __init__(self,feeder,data,slowEMA,fastEMA,window,threshold):
        
        self.feeder = feeder
        self.data = data
        self.slowEMA = slowEMA
        self.fastEMA = fastEMA
        self.window = window
        self.threshold = threshold


    def Opportunity(self):
        
        data = self._crossover()
        average = self._powerVolumes()

    
        if (data['crossover'].iloc[-1] == 1) & (average > self.threshold) :
            investment = True

        else:
            investment = False
            
        return investment


    def _powerVolumes(self):
        """Calculates the "power" of the current volume based on the 
        average volume of the last X periods.
        """

        period = len(self.data)-self.window
        windowData = self.data.shift(1)

        averageWindow = windowData['V'][period:].mean()
        averageWindow
        percentValue = (
            (self.data['V'].iloc[-1] - averageWindow) / averageWindow) * 100

        return percentValue        


    def _crossover(self):
        self.data = self.data
        self.data['slowEma'] = self._expMovingAverage(self.data['C'], self.slowEMA)
        self.data['fastEma'] = self._expMovingAverage(self.data['C'], self.fastEMA)

        self.data['crossover'] = np.where((self.data['slowEma'] > self.data['fastEma']) & (self.data['slowEma'].shift(
            1) <= self.data['fastEma'].shift(1)), 1, 0)

        return self.data['crossover']



    def _expMovingAverage(self, values, window):
        weights = np.exp(np.linspace(-1., 0., window))
        weights /= weights.sum()
        a = np.convolve(values, weights, mode='full')[:len(values)]
        a[:window] = a[window]

        return a
