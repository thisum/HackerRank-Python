import math
import os
import random
import re
import sys
import string


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    indices = [string.ascii_lowercase.index(letter) for letter in word.lower()]
    max_height = max([h[i] for i in indices])
    return len(word) * max_height


if __name__ == '__main__':

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)
    print(result)

