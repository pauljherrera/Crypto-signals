# -*- coding: utf-8 -*-

import pandas as pd



class DataFeeder:
    """
    Abstract Base Class.
    Retrieves data from a cryptocurrencies exchange.

    """
    

class BittrexFeeder(DataFeeder):
    """
    """
    

class BinanceFeeder(DataFeeder):
    """
    """
    

    


class Indicator:
    """
    Abstract Base Class.
    Indicates an investment opportunity.
    """
    def calculate(self, data):
        """
        Returns a pd.Series with datetime.datetime as index and the
        indicator values.
        
        :param data: pd.DataFrame with columns "Open", "High", "Low", "Close"
               and "Volume" and a datetime.datetime index.
        """
        raise NotImplementedError



class EMACrossoverBullish(Indicator):
    def __init__(self, slowEMA, fastEMA):
        self.slowEMA = slowEMA
        self.fastEMA = fastEMA
        
        

class VolumePower(Indicator):
    """
    Calculates the "power" of the current volume based on the 
    average volume of the last X periods.
    """
    def __init__(self, periods, threshold):
        self.periods = periods
        self.threshold = threshold



class Strategy:
    """
    Abstract Base Class.
    Union of indicators.
    Generates signals based on schedule calls.
    """
    def __init__(self, indicators=None, data_feeder=None):
        self.indicators = []
        if indicators:
            for indicator in indicators:
                self.add_indicator(indicator)
        
        if data_feeder:
            self.data_feeder = data_feeder
    
    
    def add_indicator(self, indicator):
        self.indicators.append(indicator)
        
        
    def generate_signal(self):
        # Gets data using the data feeder acordding to the timeframe.
        
        # Generates the indicators using the data.
        
        # If there's a signal, it sends it.
        
        raise NotImplementedError
        
    
    def send_signal(self, signal):
        raise NotImplementedError
        
        

class Emailer:
    """
    Sends emails.
    """
    def __init__(self, email_list):
        self.email_list = email_list


