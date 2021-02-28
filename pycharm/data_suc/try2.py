def MaxSubarray():
    # code goes here
    arr=[2,3,4,-5]
    print(arr)
    l = len(arr)
    #p=[ [],[[1],[2],[3]],[[1,2],[2,3]],[[1,2,3]] ]
    p=[[]]
    sumlist=[]

   # print(sumlist)
    for r in range(1,l+1):
        k = l - (r - 1)
        p.append([])
        cout = 0
        coutt = 0
        for u in range(1,k+1):
            p[r].append([])
            for s in range(l):
                if s>(k-1):
                    pass
                else:
                    sum = 0
                    coutt += 1
                    for t in range(s, r + s):
                        if coutt == 1:
                            p[r][s].append(arr[cout])
                            cout += 1
                        else:
                            if (cout - 1) == 0:
                                print(cout - (r - 1))
                            p[r][s].append(arr[cout - (r - 1)])
                            cout += 1
                        sum += p[r][s][t - s]
                    sumlist.append(sum)
    print(p)
    sumlist.sort(reverse=True)
    MaxSubarray.x=sumlist[0]



    return arr


# keep this function call here
#MaxSubarray(input())
MaxSubarray()
print(MaxSubarray.x)