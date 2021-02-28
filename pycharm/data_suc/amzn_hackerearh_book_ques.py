"""
amazon hacker earth quiz,difficulty:medium

Q:
if gg read n book each for m hour,if alternate book is removed ,
output:
how much hour he read now?
also provide functionality to take several input at a time i.e., t .
also if the case of several input,take all the input first ,
then print all output line by line

"""


t=int(input())

#def entry():
#   n, m = map(int, input().split())
n=[]
m=[]
for r in range(t):
    p, q = map(int, input().split())
    n.append(p)
    m.append(q)



for r in range(t):
    if (n[r]/2-(n[r]//2))>0:
       print(m[r]*(int(n[r]/2)+1))
    else:
       print(m[r]*(int(n[r]/2)))
