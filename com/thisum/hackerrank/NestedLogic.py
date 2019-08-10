#!/bin/python3

import math
import os
import random
import re
import sys

def library_penelty(actual, expected):

    if actual[2] > expected[2]:
        return 10000
    elif actual[2] < expected[2]:
        return 0
    else:
        if actual[1] > expected[1]:
            return 500 * (actual[1] - expected[1])
        elif actual[1] == expected[1] and actual[0] > expected[0]:
            return 15 * (actual[0] - expected[0])
        else:
            return 0

if __name__ == '__main__':

    dates = []

    for _ in range(2):
        dates.append(list(map(int, input().rstrip().split())))

    result = library_penelty(dates[0], dates[1])
    print(result)

