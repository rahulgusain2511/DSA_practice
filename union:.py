def sortedArray(a,b):
    x=set()
    for i in range (len(a)):
        x.add(a[i])
    for i in range (len(b)):
        x.add(b[i])
    union=[]
    for i in x:
        union.append(i)
    union.sort()
    return union


a=[1,2,3,4]
b=[3,4,5,6,7]
print(sortedArray(a,b))


