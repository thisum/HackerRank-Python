#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):

    result = list()

    sums = [sum(x) for x in orders]
    aux = sums.copy()
    aux.sort()

    prev = -1
    count = 0
    for i,x in enumerate(aux):
        if x == prev:
            count += 1
            temp = count
            for j, a in enumerate(sums):
                if a == x:
                    if temp == 0:
                        result.append(j + 1)
                    temp -= 1
        else:
            prev = x
            count = 0
            result.append(sums.index(x) + 1)

    return result

if __name__ == '__main__':

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)
    print(result)

