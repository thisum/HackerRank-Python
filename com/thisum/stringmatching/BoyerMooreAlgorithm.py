"""
efficient algorithm to perform text search based on two facts
1. find the matching characters of the pattern and text and do the shift
2. totally skip the characters which are not matching
"""

ALPHABET_SIZE = 255


def badHeuristicCalculation(pattern):
    arr = [0] * ALPHABET_SIZE
    m = len(pattern)

    for i in range(ALPHABET_SIZE):
        arr[i] = m
    for i in range(m - 1):
        arr[ord(pattern[i])] = m - 1 - i

    return arr


def isPrefix(word, pos):
    suffixlen = len(word) - pos
    for i in range(suffixlen):
        if word[i] != word[pos + i]:
            return False
    return True


def suffixLength(word, pos):
    i = 0
    while (word[pos - i] == word[len(word) - 1 - i]) and (i < pos):
        i += 1

    return i


def goodHeuristicCalculation(pattern):
    m = len(pattern)
    arr = [0] * m
    last_prefix_index = m - 1

    for i in range(m-1, 0, -1):
        if isPrefix(pattern, i + 1):
            last_prefix_index = i + 1

        arr[i] = last_prefix_index + (m - 1 - i)

    for i in range(m-1):
        slen = suffixLength(pattern, i)

        if pattern[i - slen] != pattern[m - 1 - slen]:
            arr[m - 1 - slen] = m - 1 - i + slen

    return arr


text = "aababcabcdefabcdeabcdef"
pattern = "abcdef"

d1 = badHeuristicCalculation(pattern)
d2 = goodHeuristicCalculation(pattern)
i = len(pattern) - 1
while i < len(text):
    j = len(pattern) - 1
    while j >= 0 and (text[i] == pattern[j]):
        i -= 1
        j -= 1
    if j < 0:
        print(i + 1)
        i = i + len(pattern) + 1
    else:
        i += max(d1[ord(text[i])], d2[j])
