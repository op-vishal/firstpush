""" it will check super prime and after that,
 sum those all super prime.
 i.e., like 23 and 37 in which each digit is prime also.
   for ex: 29 is prime but not super prime.
"""

first=input("enter starting limit :  ")
last=input("enter ending limit :  ")
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


for r in range(int(first),int(last)+1):
    x=r
    prime()
    if prime.q=='y':
        l1.append(x)
print("\n\nPRIMES LIST: ")
print(l1)
for r in l1:
    y=str(r)
    for q in y:
        x=int(q)
        prime()
        if not(prime.q=='y'):
            break
    if prime.q=='y':
        l2.append(int(y))
print("\n\nSUPERPRIMES LIST : ")
print(l2)
sum=0
for r in l2:
    sum+=r
print("\n\nSUM SUPERPRIMES= "+str(sum))



