#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    arr.sort()
    brr.sort()

    number = 0
    index = 0
    missing = set()

    for i in range(len(brr)):
        number = brr[i]
        if index < len(arr):
            if number == arr[index]:
                index += 1
            else:
                missing.add(number)
        else:
            missing.add(number)

    return sorted(missing)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    print(result)

