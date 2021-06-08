class Employee():
    def __init__(self,en,deg,sal,lbdct):
        self.en=en
        self.deg=deg
        self.sal=int(sal)
        self.lb=lbdct


class Organization:
    def __init__(self,elst):
        self.empl=elst

    def chkle(self,emp,ltype,nofl):
        if(x=0):
            return 1
        else:
            return False

if __name__=='__main__':
    enum=int(input())
    elst=[]
    for r in range(enum):
        elst.append(input())
