#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones_loop_method(n, a, b):

    result = set()

    for i in range(pow(2,n-1)):
        final = 0
        k = n-2
        while k > -1:
           final += a if (k > 0 and i//pow(2,k) == 0) or (k == 0 and i%2 == 0) else b
           k -= 1

        result.add(final)

    return sorted(result)

def stones(n, a, b):

    x = min(a,b)
    y = max(a,b)
    result = set()

    for i in range(n):
        result.add(x*(n-1) + i*(abs(y-x)))

    return sorted(result)

if __name__ == '__main__':
    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)
        print(result)

