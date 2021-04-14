
import pandas as pd
import numpy as np

df = pd.read_csv("/usercode/files/ca-covid.csv")

df.drop('state', axis=1, inplace=True)
df.set_index('date', inplace=True)
df['ratio']=df['deaths']/df['cases']
df=df[df['ratio']==df['ratio'].max()]
print(df)