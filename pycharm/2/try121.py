class Team:
    def __init__(self,oo,vv,ii,nn):
        self.oo=oo
        self.vv=float(vv)
        self.ii=int(ii)
        self.nn=nn

class League:
    def __init__(self, ln,tlst):
        self.ln=ln
        self.tlst=tlst

    def findMinimumTeamById(self,tlst):
        iidd = []
        tttt = []
        if len(tlst)>0:
            for r in tlst:
                iidd.append(r.ii)

            iidd.sort()
            for r in tlst:
                if(iidd[0]==r.ii):
                    tttt.append(r.oo)
                    tttt.append(r.vv)
                    tttt.append(r.ii)
                    tttt.append(r.nn)



        return tttt

    def sortTeamById(self,tlst):
        iii=[]
        nne=["NONE"]
        if len(tlst)>0:
            for r in tlst:
                iii.append(r.ii)
            iii.sort()
            return iii
        else:

            return nne






if __name__=="__main__":
    mm=input()
    n=0
    tlst=[]
    ln=""


    if len(mm)>0:
        n=int(mm)

    for r in range(n):
        o=input()
        w=float(input())
        i=int(input())
        n=input()
        tlst.append(Team(o,w,i,n))

    lgo = League(ln, tlst)
    f=lgo.findMinimumTeamById(tlst)
    ff=lgo.sortTeamById(tlst)
    if len(tlst) > 0:
        print("\n".join(map(str,f)))

    print("\n".join(map(str, ff)))

