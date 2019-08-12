#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(board):

    upper = -1
    for x in board:
        if x[0] == upper:
            return "NO"
        else:
            upper = x[0]
            for i in range(len(x)-1):
                if x[i] == x[i+1]:
                    return "No"
    return "Yes"

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        board = []

        for _ in range(n):
            board.append(list(map(int, input().rstrip().split())))

        result = solve(board)
        print(result)

