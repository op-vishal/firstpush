list=[8,4,6,12,9]
#print(sum(list))

tr=list
tr.sort()
print(tr)
l=len(tr)
final=[]
for r in reversed(range(l)):

    final.append(sum(tr[0:r+1]))

print(sum(final)-tr[0])
