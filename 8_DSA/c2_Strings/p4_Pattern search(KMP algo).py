def constructlps(pat,lps):
    m = len(pat)
    len_ = 0
    i = 1
    while i < m :
        if pat[i] == pat[len_]:
            len_ += 1
            lps[i] = len_
            i += 1

        else:
            if len_ != 0:
                len_ = lps[len_-1]
        
            else :
                lps[i] = 0
                i += 1




def search(pat,txt):
    n = len(txt)
    m = len(pat)


    lps = [0] * m
    res = []
    constructlps(pat,lps)

    i = 0
    j = 0

    while i < n:
        if txt[i] == pat[j]:
            i += 1
            j += 1

            if j == m:
                res.append(i-j)

                j = lps[j-1]

        else :
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return res 

if __name__ == "__main__":
    txt = "aabaacaadaabaaba"
    pat = "aaba"

    res = search(pat, txt)
    for i in range(len(res)):
        print(res[i], end=" ")