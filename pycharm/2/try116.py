c=int(input())
ll=[]
for r in range(c):
    ll.append([])
    id=int(input())
    ll[r].append(id)
    name=input()
    ll[r].append(name)
    gen=input()
    ll[r].append(gen)
    dst=int(input())
    ll[r].append(dst)

idd=int(input())
dp=float(input())
cnt=0
for r in ll:
    if(idd==r[0]):
        cnt=1
        print("discount of "+str(r[0])+" is:"+str(0.01*dp*r[3]))

if(cnt==0):
    print("no name")
