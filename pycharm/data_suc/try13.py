def ar(w,h,isver,dis):
    l=len(isver)
    h1=0
    h2=h
    w1=0
    w2=w
    area=w*h

    reta=[]
    for r in range(l):
        if isver[r]==1:
            if dis[r]<=(w/2) and not(dis[r]>w2):
                w1=dis[r]
                area=((w2-w1)*(h2-h1))
                reta.append(area)
            elif dis[r]>(w/2) and not(dis[r]<w1):
                w2=dis[r]
                area=(w2-w1)*(h2-h1)
                reta.append(area)
        else:
            if dis[r]<=(h/2) and not(dis[r]>h2):
                h1=dis[r]
                area=((w2-w1)*(h2-h1))
                reta.append(area)
            elif dis[r]>(h/2) and not(dis[r]<h1):
                h2=dis[r]
                area=(w2-w1)*(h2-h1)
                reta.append(area)
    return reta











res=ar(5,5,[1,0,0,1],[3,4,1,1])
print(res)