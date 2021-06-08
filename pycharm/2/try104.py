

i=input()
ii=input()
iii=input()

l=""
ll=""
lll=""

for r in i:
    if r=="a" or r=="e" or r=="i" or r=="o" or r=="u":
        r="%"
        l=l+r
    else:
        l=l+r
for r in ii:
    if not(r=="a" or r=="e" or r=="i" or r=="o" or r=="u"):
        r="#"
        ll=ll+r
    else:
        ll=ll+r

for r in iii:
    r=r.upper()
    lll=lll+r

print(l+ll+lll)

