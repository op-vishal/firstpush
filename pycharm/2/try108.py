from itertools import permutations

m=int(input())
n=int(input())

j=permutations(range(1,m+1),n)
k=list(j)
f=[]

for r in k:
    yy=0
    for s in range(n-1):
        if not(r[s+1]>= (2*(r[s]))  ):
            break
        else:
            yy = yy + 1

    if yy==(n-1):
        f.append(r)

print(f)
print(len(f))


