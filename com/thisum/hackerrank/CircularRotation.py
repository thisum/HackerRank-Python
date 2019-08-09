#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotationOld(a, k, queries):

    overflow = 0
    for _ in range(k):
        overflow = a[len(a)-1]
        for i in range(len(a)-1, 0, -1):
            a[i] = a[i-1]
        a[0] = overflow

    result = list()
    for x in queries:
       result.append(a[x])

    return result

def circularArrayRotation(a, k, queries):

    result = list()
    res_index = 0
    l = len(a)
    for i in queries:
        res_index = (l+(i-k%l))%l
        result.append(a[res_index])

    return result

if __name__ == '__main__':

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    print(result)

