import pandas as pd
import numpy as np


class EMACrossoverBullish(object):
    """Class for EMA crossover calculation
    """

    def __init__(self, data, slowEMA, fastEMA):
        """Initialize parameters
        :param data: DataFrame with DTOHLCV
        :type data: pd.Dataframe

        :param slowEMA: Slow window for EMA calculation
        :param slowEMA: int.

        :param fastEMA: Fast window for EMA calculation
        :type fastEMA: int.
        """
        self.slowEMA = slowEMA
        self.fastEMA = fastEMA
        self.data = data

    def _ExpMovingAverage(self, values, window):
        weights = np.exp(np.linspace(-1., 0., window))
        weights /= weights.sum()
        a = np.convolve(values, weights, mode='full')[:len(values)]
        a[:window] = a[window]

        return a

    def Crossover(self):
        data = self.data
        data['slowEma'] = self._ExpMovingAverage(data['C'], self.slowEMA)
        data['fastEma'] = self._ExpMovingAverage(data['C'], self.fastEMA)

        data['crossover'] = np.where((data['slowEma'] > data['fastEma']) & (data['slowEma'].shift(
            1) <= data['fastEma'].shift(1)),1,0)

        return data[]
