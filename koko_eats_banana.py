import math
def minimumRateToEatBananas(v,h):
    low=1
    high=max(v)
    ans=max(v)
    while low<=high:
        mid=(low+high)//2
        hours=0
        for i in v:
            hours+=math.ceil(i/mid)
        if hours<=h:
            ans=min(ans,mid)
            high=mid-1
        else:
            low=mid+1
    return ans



class Solution(object):
    def minEatingSpeed(self,v,h):
        low=1
        high=max(v)
        ans=max(v)
        while low<=high:
            mid=(low+high)//2
            hours=0
            for i in v:
                hours+=math.ceil(i/mid)
            if hours<=h:
                ans=min(ans,mid)
                high=mid-1
            else:
                low=mid+1
        return ans+1
