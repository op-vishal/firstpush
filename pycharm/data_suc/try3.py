n, m, x = map(int, input().split())
p=[]
for r in range(n):
    h = list(map(int, input().split()))
    p.append(h)
k=[]
l=[]
for r in range(n):
    for s in range(m):

        l.append(p[r][s])