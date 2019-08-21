"""
concatenate the pattern and the text and then do prefix matching
"""


def computeZArray(s, z):

    L = 0
    R = 0

    for i in range(1, len(s)):

        if i > R:
            L = R = i

            while R < len(s) and s[R-L] == s[R]:
                R += 1

            z[i] = R - L
            R -= 1

        else:
            k = i - L
            if z[k] < R - i + 1:
                z[i] = z[k]

            else:
                L = i
                while R < len(s) and s[R-L] == s[R]:
                    R += 1

                z[i] = R - L
                R -= 1


def search(p, t):

    concat = p + "$" + t
    z = [0] * len(concat)
    computeZArray(concat, z)

    for i, x in enumerate(z):
        if x == len(p):
            print("pattern found at index: %d" %(i-len(p)-1))


txt = "ABABCDAABCDAAAABCDA"
pat = "ABCD"
search(pat, txt)