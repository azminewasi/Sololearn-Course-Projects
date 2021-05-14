n = int(input())
X = []
for i in range(n):
    X.append([float(x) for x in input().split()])
    if i == 0 :
        p = len(X[0])

y = [int(x) for x in input().split()]
datapoint = [float(x) for x in input().split()]


import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array(X)
X = X.reshape((n, p))

y = np.array(y)

model = LogisticRegression()
model.fit(X, y)

datapoint = np.array(datapoint)
datapoint = datapoint.reshape((1, p))

z = model.predict(datapoint)

print(z[0])