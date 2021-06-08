Tea=['tea','normal','high']
coffee=['coffee','e','j']
fst=input("first letter")
final=[]
final.append(Tea)
final.append(coffee)
id=input("id")
print(final)
for r in range(len(final)):
    if final[r][0][0]==fst:
        print(final[r][0])

