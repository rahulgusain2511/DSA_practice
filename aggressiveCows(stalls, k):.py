def aggressiveCows(stalls, k):
    stalls.sort()
    low=0
    high=max(stalls)
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if isPossible(stalls,k,mid):
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans


def isPossible(stalls,k,mid):
    cow_cnt=1
    last_pos=stalls[0]

    for i in range(len(stalls)):
        if stalls[i]-last_pos>=mid:
            cow_cnt+=1
            if cow_cnt==k:
                return True
            
            last_pos=stalls[i]
            
    return False