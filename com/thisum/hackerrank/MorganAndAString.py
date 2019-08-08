#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the morganAndString function below.
def morganAndString(a, b):

    jack = a
    daniel = b

    result = ""
    while len(jack) > 0 or len(daniel) > 0:
        if len(jack) == 0:
            result += ''.join(daniel)
            break

        if len(daniel) == 0:
            result += ''.join(jack)
            break

        if jack[0] <= daniel[0]:
            result += jack[0]
            jack = jack[1:]

        else:
            result += daniel[0]
            daniel = daniel[1:]

    return result

def morganAndStringNew(a, b):

    a += "_"
    b += "_"
    result = ""

    for x in range(len(a) + len(b) -2):
        if a < b:
            result += a[0]
            a = a[1:]
        else:
            result += b[0]
            b = b[1:]

    return result

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndStringNew(a, b)

        print(result)

