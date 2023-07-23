def moveZeros(n,a):
    temp=[]
    for i in range (n):
        if a[i]!=0:
            temp.append(a[i])
    for i in range (len(temp)):
        a[i]=temp[i]
    for i in range (len(temp),n):
        a[i]=0
    return a