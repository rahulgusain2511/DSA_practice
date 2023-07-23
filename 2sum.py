def read(n,book,target):
    #optimal
    left=0
    right=n-1
    book.sort()
    while(left<right):
        sum=book[right]+book[left]
        if sum==target:
            return "YES"
        elif sum>target:
            right-=1
        else:
            left+=1
    return 'NO'
    """ Brute force
    flag="NO"
    for i in range(n):
        for j in range(i+1,n):
            if i==j:
                continue
            elif book[i]+book[j]==target:
                flag="YES"
    return flag
    """