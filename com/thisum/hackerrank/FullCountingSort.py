#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict

# Complete the countSort function below.
def countSort(arr):

    table = dict()

    for i in range(len(arr)):
        if i < len(arr)//2:
            arr[i][1] = '-'
        key = arr[i][0]
        if table.get(key) is None:
            table[key] = list()
        table.get(key).append(arr[i][1])

    table = OrderedDict(sorted(table.items()))
    output = []
    for v in table.values():
        output.append(v)
    output = str(output).replace("[", "").replace("]", "").replace("'", "").replace(",", "")

    print(output)


def map_values(val):
    return [int(val[0]), val[1]]

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(map_values(input().rstrip().split()))

    countSort(arr)
