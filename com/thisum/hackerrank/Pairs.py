#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs_brute_force(k, arr):

    arr = sorted(arr, reverse=True)

    pairs = 0
    for i in range(len(arr)-1):
        j = i+1
        while j < len(arr) and arr[i] - arr[j] <= k:
            if arr[i] - arr[j] == k:
                pairs += 1
                break
            j += 1

    return pairs


def pairs(k, arr):

    arr = sorted(arr)
    vals = set(arr)

    pairs = 0

    for x in vals:
        if x + k in vals:
            pairs += 1

    return pairs

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(result)

