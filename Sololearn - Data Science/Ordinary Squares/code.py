import numpy as np

n, p = [int(x) for x in input().split()]
X = []
for i in range(n):
    X.append([float(x) for x in input().split()])

y = [float(x) for x in input().split()]

X=np.array(X).reshape(n,p)
y=np.array(y)
b=np.linalg.pinv(X) @ y.transpose()
print(np.around(b, decimals=2))