#!/bin/python3

import math

import random
import re
import sys

#
# Complete the 'sortedSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
from operator import mul



def sortedSum(a):
    # Write your code here
    l = len(a)
    newa = a
    n = len(newa)
    check = []
    natural = []

    natural = list(range(1, l + 1))
    check = newa[:n]
    check.sort()

    if n > 1:
        x=sum(map(mul,natural,check))
        del newa[n - 1]
        return (x + sortedSum(newa))%(10**9+7)
    elif n == 1:
        return newa[0]

print(sortedSum([5,9]))





