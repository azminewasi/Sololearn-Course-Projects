import numpy as np
n, p = [int(x) for x in input().split()]
lista=[]
for i in range(n):
    lista.append(input().split())
print(np.array(lista).astype(np.float16).mean(axis=1).round(2))
