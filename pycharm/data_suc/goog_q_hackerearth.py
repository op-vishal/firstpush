n=int(input())



h = list(map(int, input().split()))
check=0
for r in range(n):
    for j in range(n):

        q=h[r]*h[j]
        if (q%10==0) and not(r==j):
            check +=1


print(int(check/2))