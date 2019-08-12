#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countLuck function below.
def countLuck(matrix, k):

    for i, r in enumerate(matrix):
        for j, c in enumerate(r):
            if c == '*':
                end = (i,j)
            elif c == 'M':
                start = (i,j)

    stack = [start]
    p_d = []
    turn_points = []
    max_h = len(matrix)
    max_l = len(matrix[0])
    found = False

    while len(stack) > 0:
        current = stack[len(stack)-1]
        p_d = []

        next_col = current[1] - 1
        if next_col > -1:
            if matrix[current[0]][next_col] == '.' and stack.count((current[0], next_col)) == 0:
                p_d.append((current[0], next_col))
            elif matrix[current[0]][next_col] == '*':
                p_d.append((current[0], next_col))
                found = True
        next_row = current[0] -1
        if next_row > -1:
            if matrix[next_row][current[1]] == '.' and stack.count((next_row, current[1])) == 0:
                p_d.append((next_row, current[1]))
            elif matrix[next_row][current[1]] == '*':
                p_d.append((next_row, current[1]))
                found = True
        next_col = current[1] + 1
        if next_col < max_l:
            if matrix[current[0]][next_col] == '.' and stack.count((current[0], next_col)) == 0:
                p_d.append((current[0], next_col))
            elif matrix[current[0]][next_col] == '*':
                p_d.append((current[0], next_col))
                found = True
        next_row = current[0] + 1
        if next_row < max_h:
            if matrix[next_row][current[1]] == '.' and stack.count((next_row, current[1])) == 0:
                p_d.append((next_row, current[1]))
            elif matrix[next_row][current[1]] == '*':
                p_d.append((next_row, current[1]))
                found = True

        if len(p_d) > 1 and turn_points.count(current) == 0:
            turn_points.append(current)

        if found:
            break

        if len(p_d) == 0:
            travelled = stack.pop()
            stack.insert(0, travelled)
            if turn_points.count(travelled) > 0:
                turn_points.remove(travelled)
        else:
            stack.append(p_d[0])

    return "Impressed" if k == len(turn_points) else "Oops!"



if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input())

        result = countLuck(matrix, k)
        print(result)

