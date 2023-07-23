def missingNumber( A, N):
    #BETTER SOLUTION 
    temp=[0]*(N+1)
    for i in range (N-1):
        temp[A[i]]+=1
    for i in range (1,N):
        if temp[i]==0:
            return i
    """
    #optimal with O(N) TC
    xor1=0
    xor2=0
    for i in range(1,N+1):
        xor1=xor1^i
        xor2=xor2^(i+1)
    
    xor1=xor1^N
    
    return xor1^xor2
    
    
    TC->O(2n)
    xor1=0
    xor2=0
    for i in range(1,N+1):
        xor1=xor1^i
    for i in A:
        xor2=xor2^i
    return xor1^xor2
    
    Optimal with O(N) TC
    s1=(N*(N+1))//2
    s2=0
    for i in A:
        s2=s2+i
    return abs(s1-s2)

    Brute force 
    for i in range(1,N+1):
        if i not in A:
            return i
    """ 


A=[1,2,3,4,5,6,8]
print (missingNumber(A,8))