import pandas as pd 

class DataFeeder(object):
    """Base class for CryptoSignals, it should be extended with a specific source"""
    def __init__(self):
        pass

    def get_open(self,data):
        """Get the open price for a specific market

        :param data: dataframe with DTOHLCV from a specific coin
        :type data: pd.DataFrame

        """
        openV = data['O']
    
        
        return openV
    
    def get_high(self,data):
        """Get the open price for a specific market

        :param data: dataframe with DTOHLCV from a specific coin
        :type data: pd.DataFrame

        """
        highV = data['H']
    
        
        return highV

    def get_low(self,data):
        """Get the open price for a specific market

        :param data: dataframe with DTOHLCV from a specific coin
        :type data: pd.DataFrame

        """
        lowV = data['L']
    
        
        return lowV

    def get_close(self,data):
        """Get the open price for a specific market

        :param data: dataframe with DTOHLCV from a specific coin
        :type data: pd.DataFrame

        """
        closeV = data['C']
        
        return closeV

    def get_volume(self,data):
        """Get the open price for a specific market

        :param data: dataframe with DTOHLCV from a specific coin
        :type data: pd.DataFrame

        """
        volumeV = data['V']
    
        
        return volumeV