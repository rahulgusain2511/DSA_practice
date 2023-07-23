def longestSubarrayWithSumK(a,k):
    left=right=0
    sum=a[0]
    maxlen=0
    n=len(a)
    while (right<n):
        while (left<=right and sum>k):
            sum-=a[left]
            left+=1
        if sum==k:
            maxlen=max(maxlen,right-left+1)
        right+=1
        if right<n:
            sum+=a[right]
    return maxlen


    """ brute
    max_len=0
    for i in range(len(a)):
        current_sum=0
        for j in range(i,len(a)):
            current_sum=current_sum+a[j]
            if current_sum==k:
                max_len=max(max_len,j-i+1)
    return max_len
    """