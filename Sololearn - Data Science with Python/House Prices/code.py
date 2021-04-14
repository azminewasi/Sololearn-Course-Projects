import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])
prices=np.array(data)
std=np.std(prices)
mean=np.mean(prices)
prices_later=prices[(prices<mean+std) & (prices>mean-std)]

print(len(prices_later)/len(prices)*100)