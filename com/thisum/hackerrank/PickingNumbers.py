#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    firstNumber = a[0]
    count = 0
    maxCount = 0
    for i, x in enumerate(a):

        if x - firstNumber <= 1:
            count += 1
        else:
            maxCount = max(maxCount, count)
            firstNumber = x
            count = 1

    maxCount = max(maxCount, count)
    return maxCount

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

