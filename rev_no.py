N=int(input())
if N==0:
    print(0)
else:
    rev=""
    while N>0:
        digit=N%10
        N=N//10
        rev=rev+str(digit)
    print(int(rev))    
