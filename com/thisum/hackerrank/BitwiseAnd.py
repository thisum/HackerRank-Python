#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        # result = -1
        # for i in range(1, n):
        #     j = i + 1
        #     while j <= n:
        #         if k > i & j > result:
        #             result = i & j
        #         j += 1

        result = k-1 if ((k-1) | k) <= n else k-2
        print(result)