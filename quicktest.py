import pandas as pd 
import numpy as np
from Feeders.bittrexFeeder import BittrexFeeder
from indicators import EMACrossoverBullish,VolumePower
import matplotlib.pyplot as plt
import time
start_time = time.time()


def main():
    
    dtohlcv = my_bittrex.get_ticks()
    
    datos = crossover.Crossover(dtohlcv)
    promedio = power.calculate(dtohlcv) 
    print(dtohlcv)
    print(promedio)
    print("ENSERIO")

if __name__ == '__main__':
    my_bittrex = BittrexFeeder('BTC-ETH','hour')
    crossover = EMACrossoverBullish(5,20)
    power = VolumePower(30)
    main()
    print("--- %s seconds ---" % (time.time() - start_time)) 
       