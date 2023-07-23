import sys
def findMin(self, nums):
        ans=sys.maxsize-1
        low=0
        n=len(nums)
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[mid]:
                ans=min(nums[low],ans)
                low=mid+1
            else:
                ans=min(nums[mid],ans)
                high=mid-1
        return ans
