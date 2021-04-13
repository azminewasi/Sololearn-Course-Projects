import numpy as np
import pandas as pd

r = int(input()) 
lst = [float(x) for x in input().split()]
arr = np.array(lst)
df=pd.Series(arr).values
df=df.reshape((r,int(len(lst)/r)))
print(df)