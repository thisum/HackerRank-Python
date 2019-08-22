"""

"""

ALPHABET_SIZE = 256


def badHeuristicCalculation(pattern):

    arr = [0] * ALPHABET_SIZE
    m = len(pattern)

    for i in range(ALPHABET_SIZE):
        arr[i] = m
    for i in range(m-1):
        arr[pattern[i]] = m - 1 - i

    return arr


def goodHeuristicCalculation(pattern):

    pass