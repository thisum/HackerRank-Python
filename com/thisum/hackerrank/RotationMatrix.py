#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation_longSolution(matrix, r):

    for i in range(r):

        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])
        topOverlfow = 0

        for j in range(min(bottom//2, right//2)):

            topOverlfow = matrix[top][left]

            for t in range(left+1, right):
                matrix[top][t-1] = matrix[top][t]

            if(bottom>1):
                matrix[top][t] = matrix[top+1][right-1]

            for r in range(top+1,bottom-1):
                matrix[r][right-1] = matrix[r+1][right-1]

            for b in range(right-1, left, -1):
                matrix[bottom-1][b] = matrix[bottom-1][b-1]

            if(bottom>1):
                matrix[bottom-1][b-1] = matrix[bottom-2][left]

            for l in range(bottom-2, top+1, -1):
                matrix[l][left] = matrix[l-1][left]

            matrix[top+1][left] = topOverlfow

            top += 1
            bottom -= 1
            left += 1
            right -= 1

    for row in matrix:
        print(str(row).replace(",", "").replace("[", "").replace("]", ""))

def reverse(arr, i, j):
    for idx in range(int((j - i + 1) / 2)):
        arr[i + idx], arr[j - idx] = arr[j - idx], arr[i + idx]


def rotateList(A, K):
    l = len(A)
    K %= len(A)

    reverse(A, l - K, l - 1)
    reverse(A, 0, l - K - 1)
    reverse(A, 0, l - 1)

    return A


def rotateLayers(r, layers):
    for layer in layers:
        rotateList(layer, len(layer) - r)


def rotateMatrix(mat, r):

    m = len(matrix)
    n = len(matrix[0])

    l = int(min(n, m) // 2)
    layers = [[] for _ in range(l)]
    for level in range(l):
        top = (n - 1) - 2 * level
        side = (m - 1) - 2 * level
        for i in range(top):  # right
            layers[level].append(mat[level][level + i])
        for j in range(side):  # down
            layers[level].append(mat[level + j][level + top])
        for i in range(top):  # left
            layers[level].append(mat[level + side][level + top - i])
        for j in range(side):  # up
            layers[level].append(mat[level + side - j][level])

    rotateLayers(r, layers)

    # fill the layers back in
    for level in range(l):
        top = (n - 1) - 2 * level
        side = (m - 1) - 2 * level
        for i in range(top):
            mat[level][level + i] = layers[level].pop(0)
        for j in range(side):
            mat[level + j][level + top] = layers[level].pop(0)
        for i in range(top):
            mat[level + side][level + top - i] = layers[level].pop(0)
        for j in range(side):
            mat[level + side - j][level] = layers[level].pop(0)

    for row in matrix:
        print(str(row).replace(",", "").replace("[", "").replace("]", ""))

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    rotateMatrix(matrix, r)
























