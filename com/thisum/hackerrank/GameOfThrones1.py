#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):

    chars = list(set(s))
    counts = [0] * len(chars)

    for c in s:
        i = chars.index(c)
        counts[i] += 1

    odds = 0
    for i in counts:
        if i % 2 == 1:
            odds += 1

        if odds > 1:
            return "NO"

    return "YES"


if __name__ == '__main__':

    s = input()

    result = gameOfThrones(s)

    print(result)