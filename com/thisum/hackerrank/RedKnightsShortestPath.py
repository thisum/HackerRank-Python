#!/bin/python3

import math
import os
import random
import re
import sys


def closeToEnd(curr, next, end, n, scores, pos):
    close = -1 < next[0] < n and -1 < next[1] < n and (
                (abs(curr[0] - end[0]) > abs(next[0] - end[0])) or (abs(curr[1] - end[1]) > abs(next[1] - end[1])))
    scores[pos] = abs(next[1] - end[1]) + abs(next[0] - end[0])
    return close


# Complete the printShortestPath function below.
def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Print the distance along with the sequence of moves.
    keys = ["UL", "UR", "R", "LR", "LL", "L"]
    results = []

    stack = [(i_start, j_start)]
    end = (i_end, j_end)
    commands = []
    found = False

    while len(stack) > 0:
        current = stack[len(stack) - 1]
        scores = [0, 0, 0, 0, 0, 0]
        result = [(), (), (), (), (), ()]

        r = current[0]
        c = current[1]
        if closeToEnd(current, (r - 2, c - 1), end, n, scores, 0) and stack.count((r - 2, c - 1)) == 0:
            result[0] = (r - 2, c - 1, "UL")

        if closeToEnd(current, (r - 2, c + 1), end, n, scores, 1) and stack.count((r - 2, c + 1)) == 0:
            result[1] = (r - 2, c + 1, "UR")

        if closeToEnd(current, (r, c + 2), end, n, scores, 2) and stack.count((r, c + 2)) == 0:
            result[2] = (r, c + 2, "R")

        if closeToEnd(current, (r + 2, c + 1), end, n, scores, 3) and stack.count((r + 2, c + 1)) == 0:
            result[3] = (r + 2, c + 1, "LR")

        if closeToEnd(current, (r + 2, c - 1), end, n, scores, 4) and stack.count((r + 2, c - 1)) == 0:
            result[4] = (r + 2, c - 1, "LL")

        if closeToEnd(current, (r, c - 2), end, n, scores, 5) and stack.count((r, c - 2)) == 0:
            result[5] = (r, c - 2, "L")

        i = scores.index(min(scores))
        if len(result[i]) > 0:
            stack.append((result[i][0], result[i][1]))
            commands.append(result[i][2])

            if (result[i][0], result[i][1]) == end:
                found = True
                break
        else:
            found = False
            break

    if found:
        print(len(commands))
        for k in keys:
            results.append((k, commands.count(k)))
        commands = []
        for x in results:
            for i in range(x[1]):
                commands.append(x[0])
        print(str(commands).replace(",", "").replace("[", "").replace("]", "").replace("'", ""))
    else:
        print("Impossible")


if __name__ == '__main__':
    n = int(input())

    i_startJ_start = input().split()

    i_start = int(i_startJ_start[0])

    j_start = int(i_startJ_start[1])

    i_end = int(i_startJ_start[2])

    j_end = int(i_startJ_start[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)
