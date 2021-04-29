S = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

SL = len(S)
BL=len(B)
AL = len(A)


one = S.count(1)
zero = S.count(0)
giniP = one/(one+zero)
giniInit = 2*giniP*(1-giniP)


one = A.count(1)
zero = A.count(0)
giniP = one/(one+zero)
giniLeft = 2*giniP*(1-giniP)


one = B.count(1)
zero = B.count(0)
giniP = one/(one+zero)
giniRight= 2*giniP*(1-giniP)

IG= giniInit -(giniLeft*(AL/SL))-(giniRight*(BL/SL))
IG=round(IG,5)
print(IG)