i=int(input())
e=int(input())
ilst=[]
elst=[]
for r in range(i):
    ilst.append(float(input())*18)

for r in range(e):
    elst.append(float(input())*12)

print("Total Cost Estimated: "+ str(round(sum(ilst)+sum(elst),1))+" INR")
