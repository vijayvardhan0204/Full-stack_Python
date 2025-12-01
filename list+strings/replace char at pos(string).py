def replace(s,pos,ch):
    return s[:pos]+ch+s[pos+1:]

s=input("enter string:")
pos,ch=input("enter position and character to be replaced:").split()
pos=int(pos)
res=replace(s,pos,ch)
print(res)


'''s = "abracadabra"
pos = 5
ch = "k"

s = s[:pos] + ch + s[pos+1:]
print(s)
'''