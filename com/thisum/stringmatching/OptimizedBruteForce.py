"""
if the characters in the pattern are distinct, can do a little optimization

if n characters of the pattern is matched with the text, and if a mismatch occurs at jth index of the p, then the p can be
shifted with j positions, as we know the characters of the p is distinct

txt = "ABABCDAABCDAAAABCDA" <-  indexing i
pat = "ABCD"                <-  indexing j

at i == 0, p and t is match until j = 1, then at j = 2 a mismatch happens.  so the i is shifted by i = i+j for the next iteration
at i == 2, match happens, so its clear the next potential match will happen at i = i + j, in this case j = len(pat)
"""


def search(pat, txt):
    m = len(pat)
    n = len(txt)
    i = 0

    if len(set(pat)) == len(pat):
        while i <= n - m:

            for j in range(m):
                if txt[i + j] != pat[j]:
                    break
                j += 1

            if j == m:
                print("Pattern found at index " + str(i))
                i = i + m
            elif j == 0:
                i = i + 1
            else:
                i = i + j

    else:
        pass
        #brute force approach


# Driver program to test the above function
txt = "ABABCDAABCDAAAABCDA"
pat = "ABCD"
search(pat, txt)