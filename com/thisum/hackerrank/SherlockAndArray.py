#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):

    right = sum(arr)
    left = 0
    index = -1

    for i in range(len(arr)):
        right -= arr[i]
        left += 0 if i == 0 else arr[i-1]

        if left == right:
            index = i
            break

    return "YES" if index > -1 else "NO"


if __name__ == '__main__':

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)
        print(result)

