import numpy as np

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

player=np.array(players)
std=np.std(player)
mean=np.mean(player)
player=player[(player<mean+std) & (player>mean-std)]

print(len(player))