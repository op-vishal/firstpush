import itertools






def check(x):
    # Returns true if x is a power of 2
    return x and (not (x & (x - 1)))


def countPairs(arr):
    n=len(arr)
    cnt = 0
    ext=0

    temp = list(itertools.product(arr, arr))
    print(temp)

    for elem in temp:


        if elem[0]==elem[1]:
            if check(elem[0] & elem[1]):
                ext+=ext
                


        elif elem[0]!=elem[1]:
           if check(elem[0] & elem[1]):
                   cnt = cnt + 1

    print(ext)
    print(cnt)
    return int((cnt)/2 + ext/2)


# Given array
arr = [1,2,1,3]


# Function Call
print(countPairs(arr))