import panas as pd 





class Indicator(object)
    def __init__(self):
        pass



    def __ExpMovingAverage(self, values, window):
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

        return data['crossover']
