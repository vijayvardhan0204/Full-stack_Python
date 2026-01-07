def MaxLength(s):
    n = len(s)
    maxLen = 0
    st = []
    st.append(-1)
    for i in range(n):
        if s[i] == '(':
            st.append(i)
        else:
            st.pop()
        
        if not st :
            st.append(i)
        else:
            maxLen = max(maxLen,i - st[-1])
    return maxLen

if __name__ == "__main__" :
    s = '(()))()()()'
    print(MaxLength(s))