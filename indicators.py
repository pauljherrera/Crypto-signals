import pandas as pd
import numpy as np


class EMACrossoverBullish(object):
    """Class for EMA crossover calculation
    """

    def __init__(self, slowEMA, fastEMA):
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

    def _ExpMovingAverage(self, values, window):
        weights = np.exp(np.linspace(-1., 0., window))
        weights /= weights.sum()
        a = np.convolve(values, weights, mode='full')[:len(values)]
        a[:window] = a[window]

        return a

    def Crossover(self, data):
        dataC = data
        dataC['slowEma'] = self._ExpMovingAverage(data['C'], self.slowEMA)
        dataC['fastEma'] = self._ExpMovingAverage(data['C'], self.fastEMA)

        dataC['crossover'] = np.where((data['slowEma'] > data['fastEma']) & (data['slowEma'].shift(
            1) <= data['fastEma'].shift(1)), 1, 0)

        return dataC['crossover']


class VolumePower(object):
    """Class for EMA crossover calculation
    """

    def __init__(self, window):
        """Initialize parameters

        :param data: DataFrame with DTOHLCV
        :type data: pd.Dataframe

        :param window: look back window
        :param window: int
        """

        self.window = window

    def calculate(self, data):
        """Calculates the "power" of the current volume based on the 
        average volume of the last X periods.
        """

        period = len(data)-self.window
        windowData = data.shift(1)

        averageWindow = windowData['V'][period:].mean()

        percentValue = (
            (data['V'].iloc[-1] - averageWindow) / averageWindow) * 100

        return percentValue
