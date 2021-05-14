import pandas as pd
import numpy as np

filename = input()
column_name = input()

df=pd.read_csv(filename)
print(df.loc[:,column_name].values)