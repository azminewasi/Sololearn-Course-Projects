import numpy as np
import pandas as pd

lst = [float(x) if x != 'nan' else np.NaN for x in input().split()]
df=pd.Series(lst)
df=df.fillna(df.mean()).round(1)
print(df)