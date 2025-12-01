# Multiply Adjacent elements

t=(1,2,3,4,5)
for i in range(len(t)-1):
    res=(t[i]*t[i+1])
    print(res)

          
resp=[]
for i in range(len(t)-1):
    resp.append(t[i]*t[i+1])
print(resp)



rest = [t[i] * t[i+1] for i in range(len(t) - 1)]
print(rest)


resto = tuple(i * j for i, j in zip(t,t[1:])) 
print(resto)