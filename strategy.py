import pandas as pd 
import numpy as np
import smtplib

class Strategy(object):
    """This class indicates an investment opportunity 
    """


    def __init__(self,feeder,data,slowEMA,fastEMA,window,threshold):
        """Initial parameter for the strategy
        :param feeder: Name of the exchange we are currently working.
        :type feeder: Str.

        :param data: DTOHLCV values from exchange at set interval
        _type data: pandas.DataFrame

        :param slowEMA: Slow window por EMA
        :type slowEMA: int

        :param fastEMA: fast window por EMA
        :type fastEMA: int

        :param window: window for volumePower calculations
        :type window: int

        :param threshold: arbitrary threshold for volumePower notifications.
        :type threshold: int
        """
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
            self.send_email("Invest")

        else:
            investment = False
            msg = "Crossover:    " + str(data['crossover'].iloc[-1]) + "Porcentaje  " + str(average)
            self.send_email(msg)
            
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

        return self.data



    def _expMovingAverage(self, values, window):
        weights = np.exp(np.linspace(-1., 0., window))
        weights /= weights.sum()
        a = np.convolve(values, weights, mode='full')[:len(values)]
        a[:window] = a[window]

        return a


    def send_email(self,msg):
        """
        Takes all the params to build the email and send it
        """
        fromaddr = 'luisomar242@gmail.com' #from
        toaddrs  = 'luisomar242@gmail.com' #to

        msg = "\r\n".join([
        "From: {}".format(fromaddr),
        "To: {}".format(toaddrs),
        "Subject: Investment Opportunity!",
        "",
        msg
        ])
        username = 'luisomar242@gmail.com'         #username
        password = 'iec10300125'         #password
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()