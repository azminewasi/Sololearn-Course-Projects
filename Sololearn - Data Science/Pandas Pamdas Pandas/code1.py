n = int(input())
import numpy as np
a=np.array([0,0])
b=np.array([2,2])
c=[]
for i in range(n):
    c.append([float(x) for x in input().split()])
c=np.array(c)
d1,d2=[],[]
for i in c:
    d1.append((((i-a)**2).sum())**0.5)
    d2.append((((i-b)**2).sum())**0.5)
rx,ry,n1=0,0,0
tx,ty,n2=0,0,0    
for i in range(len(d1)):
    if d1[i]<=d2[i]:
        rx+=c[i][0]
        ry+=c[i][1]
        n1+=1
    else:
        tx+=c[i][0]
        ty+=c[i][1]
        n2+=1

if (n1 is None) or (n1==0):
    print(None)
else:
    v=[rx/n1, ry/n1]
    v=np.array(v)
    v=np.round(v,2)
    print(v)
if (n2 is None) or (n2==0):
    print(None)
else:
    b=[tx/n2, ty/n2]
    b=np.array(b)
    b=np.round(b,2)
    print(b)
