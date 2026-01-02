def pow(b,e):

    if e == 0 :
        return 1
    
    if e < 0 :
        return 1/pow(b, -e)
    
    temp = pow(b,e//2)

    if e % 2 == 0:
        return temp * temp
    
    else:
        return b * temp * temp
    
if __name__ == "__main__":
    b = 3
    e = 5
    print(pow(b,e))