def isSorted(n,a):
    for i in range (n-1):
        if (a[i+1]<a[i]):
            return 0
    return 1
        


a=[4,5,4,4,4]
n=5
print(isSorted(n,a))