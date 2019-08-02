#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    count = 0
    max_d = max(ar)
    res = [(lambda x:  count + 1) for x in ar if x == max_d]
    print(len(res))


if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    
