import pandas as pd 
import numpy as np
import smtplib

class Strategy(object):
    """This class indicates an investment opportunity 
    """


    def __init__(self,feeder,slowEMA,fastEMA,window,threshold):
        """Initial parameter for the strategy
        :param feeder: Name of the exchange we are currently working.
        :type feeder: Str.

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
        self.slowEMA = slowEMA
        self.fastEMA = fastEMA
        self.window = window
        self.threshold = threshold


    def Opportunity(self,data,market):
    
       try:
            values = self._crossover(data)
            average = self._powerVolumes(data)
            market_name = market
        
            if (values['crossover'].iloc[-1] == 1) & (average > self.threshold) :
                investment = True
                msg = "Invest on: " + market_name + " " + "in" + self.feeder
                self.send_email(msg)

            else:
                investment = False
                #msg = "Crossover:    " + str(values['crossover'].iloc[-1]) + "Porcentaje  " + str(average)
            # self.send_email(msg)
       except KeyError as e:
            print(e)
            investment = 'Error'
            
       return investment


    def _powerVolumes(self,data):
        """Calculates the "power" of the current volume based on the 
        average volume of the last X periods.
        """

        period = len(data)-self.window
        windowData = data.shift(1)

        averageWindow = windowData['V'][period:].mean()
        
        percentValue = ((data['V'].iloc[-1] - averageWindow) / averageWindow) * 100

        return percentValue        


    def _crossover(self,data):
        
        data['slowEma'] = self._expMovingAverage(data['C'], self.slowEMA)
        data['fastEma'] = self._expMovingAverage(data['C'], self.fastEMA)

        data['crossover'] = np.where((data['slowEma'] > data['fastEma']) & (data['slowEma'].shift(
            1) <= data['fastEma'].shift(1)), 1, 0)

        return data



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
        username = ''         #username
        password = ''         #password
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()