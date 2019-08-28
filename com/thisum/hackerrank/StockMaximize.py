#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    # Write your code here

    profit = 0
    max = 0
    max_index = 0

    for i, x in enumerate(prices):
        if x > max:
            max = x
            max_index = i

    for j in range(0, max_index + 1):
        profit += max - prices[j]

    if max_index + 1 == len(prices):
        return profit
    else:
        return profit + stockmax(prices[max_index + 1:] )


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        print(result)
