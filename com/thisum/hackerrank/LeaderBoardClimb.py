#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):

    res = list()

    l = list(set(scores))
    l.sort()
    alice.sort()

    j = 0
    for a in alice:
        for i in range(j, len(l)):
            if l[i]>a:
                res.append(len(l)-i+1)
                j=i
                break

            if i == len(l)-1:
                res.append(1)

        # for i,x in enumerate(l):
        #
        #     if x>a:
        #         res.append(len(l)-i+1)
        #         break
        #
        #     if i == len(l)-1:
        #         res.append(1)

    return res


if __name__ == '__main__':

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

