#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    w.sort()

    containers = 1
    max_load = w[0]
    for i,x in enumerate(w):
        if x > max_load + 4:
            containers +=1
            max_load = x

    return containers

if __name__ == '__main__':
    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)
    print(result)

