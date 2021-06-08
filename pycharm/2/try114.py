class Psngr:
    def __init__(self,id,name,g,dst):
        self.id=int(id)
        self.name=name
        self.g=g
        self.dst=int(dst)

class Find:
    def dsc(self,l,idd,dntp):
        kk=[]
        for i in l:
            if(idd==i.id):
                dd=float(0.01*dntp*(i.dst))
                kk.append(dd)
        return kk



if __name__=='__main__':
    p=[]
    c=int(input())
    for r in range(c):
        id=int(input())
        name=input()
        g=input()
        dst=int(input())
        p.append(Psngr(id,name,g,dst))
    idd=int(input())
    dntp=float(input())
    nn=Find()
    rr=nn.dsc(p,idd,dntp)
    if not(len(rr)==0):
        print("discount of "+str(idd)+" is:"+str(rr[0]))
    else:
        print("no name")
