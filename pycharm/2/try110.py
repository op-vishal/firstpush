s="noon"
ch="o"
count=0
if not(len(s)<2):
    if not(s[0]==s[len(s)-1]):
        print(int(0))
    else:
        for r in s:
            if r==ch:
                count=count+1
                if r==s[len(s)-1]:
                    print(count)

else:
    print(int(-1))

