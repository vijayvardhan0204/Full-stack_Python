def findAnagrams(s,p):
        sCount ={}
        pCount ={}
        res =[]
        if len(p) > len(s):
            return []
        for i in range(len(p)):
            pCount[p[i]] = pCount.get(p[i],0) + 1
            sCount[s[i]] = sCount.get(s[i],0) + 1
        if pCount == sCount:
            res.append(0)

        l = 0
        for r in range(len(p),len(s)):
            sCount[s[r]] = sCount.get(s[r],0) + 1
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if pCount == sCount:
                res.append(l)
        return res


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print(findAnagrams(s,p))