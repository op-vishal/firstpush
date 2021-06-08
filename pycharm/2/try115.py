class Stock:
    def __init__(self,sname,sector,sval):
        self.sname=sname
        self.sector=sector
        self.sval=sval
class Find:
    def gslist(self,l,sss):
        mm=[]
        for i in l:
            if((i.sector==sss) and (i.sval>500)):
                mm.append(i.sname)
        return mm





if __name__=='__main__':
    p=[]
    c=int(input())
    for r in range(c):
        sname=input()
        sector=input()
        sval=int(input())
        p.append(Stock(sname,sector,sval))
    sss = input()
    nn=Find()
    ff=nn.gslist(p,sss)
    for r in ff:
        print(r)
