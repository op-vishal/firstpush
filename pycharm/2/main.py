class Patient:
    def __init__(self,cd,nm,ag,dn,ba):
        self.cd=cd
        self.nm=nm
        self.ag=int(ag)
        self.dn=dn
        self.ba=float(ba)


class Doctor:
    def __init__(self,plst):

        self.plst=plst


    def findPatientWithMaximumAge(self,plst):
        pat=[]
        age=[]
        max=[]
        nnnn=["No Data Found"]
        for i in plst:
            age.append(i.ag)
            pat.append(i.nm)
        age.sort(reverse=True)
        if len(plst)>0:
            for i in plst:
                if (i.ag==age[0]):
                    max.append(i.cd)
                    max.append(i.nm)
                    max.append(i.ag)
                    max.append(i.dn)
                    max.append(i.ba)

            return max
        else:
            return(nnnn)

    def sortPatientByBillAmount(self,plst):
        bill=[]
        #ppp=[]
        nne=["No Data Found"]
        for r in plst:
            bill.append(r.ba)
        bill.sort()
        '''for r in bill:
            for s in plst:
                if(r==s.ba):
                    ppp.append(s.pn)'''

        if len(plst)>0:
            return bill
        else:

            return (nne)



if __name__=="__main__":
    mm=input()
    n=0
    if len(mm)>0:
        n=int(mm)
    plst=[]

    for r in range(n):
        cd=input()
        nm=input()
        ag=int(input())
        dn=input()
        ba=float(input())
        plst.append(Patient(cd,nm,ag,dn,ba))

    dd=Doctor(plst)
    f=dd.findPatientWithMaximumAge(plst)
    ff=dd.sortPatientByBillAmount(plst)
    if len(plst) > 0:
        print("\n".join(map(str,f)))

    print("\n".join(map(str,ff)))





