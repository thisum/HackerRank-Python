
def brutforce(t, p):

    for i in range(len(t)-len(p)+1):
        mismatch = False
        for j, x in enumerate(p):
            if t[i+j] != x:
                mismatch = True
                break

        if not mismatch:
            print("found a match at: %d" %i )


txt = "CABABADDABABACDD"
pat = "ABABA"

brutforce(txt, pat)

