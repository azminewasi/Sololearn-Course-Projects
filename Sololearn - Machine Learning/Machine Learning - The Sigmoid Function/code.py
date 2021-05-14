import math
w1, w2, b, x1, x2 = [float(x) for x in input().split()]
y=w1*x1+w2*x2+b
res=1/(1+math.exp(-y))
print(round(res,4))
