"""
scan from the right
just comparing the two adjacent, see if there's small number of the two, if found (i-1), there's a next max otherwise no
if found, then from there, scan to the right to see whats the next max (j)
then swap the two
then sort the list from the i-th position to the right
result is the next max
"""

def find_the_next_max(word):

    chars = [ord(c) for c in word]
    found = False

    for i in range(len(chars)-1, 0, -1):
        if chars[i] > chars[i-1]:
            found = True
            break

    if not found:
        return "no answer"

    sm = chars[i-1]
    nxt_max = i
    for j in range(i, len(chars), 1):
        if sm < chars[j] < chars[nxt_max]:
            nxt_max = j

    temp = chars[i-1]
    chars[i-1] = chars[nxt_max]
    chars[nxt_max] = temp

    chars[i:] = sorted(chars[i:])

    return "".join(chr(i) for i in chars)


d = find_the_next_max("dcba")
print(d)
