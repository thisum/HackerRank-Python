#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):

    count = 0
    for x in s:
        if x.isupper():
            count += 1

    return count+1

if __name__ == '__main__':

    s = input()

    result = camelcase(s)

    print(result)
