import pandas as pd 
import numpy as np
from Feeders.bittrexFeeder import BittrexFeeder
from emacrossover import EMACrossoverBullish
import matplotlib.pyplot as plt
import time
start_time = time.time()
def main():
    

    my_bittrex = BittrexFeeder()

    
    dtohlcv = my_bittrex.get_ticks('BTC-ETH','day')
    
    crossover = EMACrossoverBullish(dtohlcv,5,20)

    print("--- %s seconds ---" % (time.time() - start_time)) 
    print(crossover.Crossover())

    #dtohlcv.plot(x= dtohlcv.index, y=['C','emaSlow','emaFast'])

    #plt.show()
    

if __name__ == '__main__':
    main()
       