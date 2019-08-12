#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    if n == 1:
        return t1
    elif n == 2:
        return t2
    else:
        return fibonacciModified(t1, t2, n-2) + pow(fibonacciModified(t1, t2, n-1), 2)


if __name__ == '__main__':

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    print(result)

