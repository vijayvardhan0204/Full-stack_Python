'''Using Divide and Conquer - O(log e) Time and O(log e) Space
The idea is to use Divide and Conquer and recursively bisect e in two equal parts. There are two possible cases:

If e is even: power(b, e) = power(b, e / 2) * power(b, e / 2); 
If e is odd: power(b, e) = b * power(b, e / 2) * power(b, e / 2); '''

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