p=9
q=7
r=5
for r in range(4,8):
    p=(p+r)+r
    if(1+r+q)>(q-p):
        q=4**p
    else:
        break

print(p+q)



