import math


n=int(input())
f=math.floor(n/2)

if not(n%2==0):
    print(f*2)
else:
    print(f-1)