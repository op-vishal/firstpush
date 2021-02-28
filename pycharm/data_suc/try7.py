First, Last = input().split()
l1=[]
l2=[]
def prime():
    p=1
    if x == 1:
        p = 'n'
    if x == 2:
        p = 'y'

    if x>2:
        for r in range(2, int(x)):


            if x % r == 0:
                p = 'n'
                break
            if p == 1:
                p = 'y'
    prime.q = p


for r in range(int(First),int(Last)+1):
    x=r
    prime()
    if prime.q=='y':
        l1.append(x)
for r in l1:
    y=str(r)
    for q in y:
        x=int(q)
        prime()
        if not(prime.q=='y'):
            break
    if prime.q=='y':
        l2.append(int(y))
total=0
for r in l2:
    total+=1
print(total)


