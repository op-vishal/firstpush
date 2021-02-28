#!/bin/python3

import os
import sys
import math


#
# Complete the twoTwo function below.
#
def twoTwo(a):
    #
    # Write your code here.
    #
    b = list(a)
    b = list(map(int, b))
    # print(b)
    # strength=[]
    l = len(a)
    ddd = []
    count = 0
    for r in range(1, l + 1):
        for s in range(l - (r - 1)):
            c = ""
            for t in range(s, s + r):
                c += a[t]
            if not (c[0] == "0"):
                d = int(c)
                if not (d == 0):
                    lg = math.log2(d)
                    if (math.floor(lg) == math.ceil(lg)) and (lg <= 800):
                        ddd.append([d])
                        count += 1

    print(ddd)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a = input()

        result = twoTwo(a)

        fptr.write(str(result) + '\n')

    fptr.close()
