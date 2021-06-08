class Payslip:
    def __init__(self,b,h,t):
        self.b=int(b)
        self.h=h
        self.t=t

class Pd:
    def __init__(self):
        self.rrr=101

    def gethpf(self,l):
        mm = []
        for r in l:
            rr=r.b*0.12
            mm.append(rr)
        mx=max(mm)
        return mx



if __name__=='__main__':

    p=[]
    c=int(input())
    for r in range(c):
        b=input()
        h=input()
        t=input()
        p.append(Payslip(b,h,t))

    nn=Pd()
    ff=nn.gethpf(p)
    print(ff)
