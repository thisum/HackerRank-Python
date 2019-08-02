#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):

    orange = 0
    apple = 0
    a_r = [(lambda d1: apple + 1) for d1 in apples if s <= a + d1 <= t]
    o_r = [(lambda d2: orange + 1) for d2 in oranges if s <= b + d2 <= t]
    print(len(a_r))
    print(len(o_r))



if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
