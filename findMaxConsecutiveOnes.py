def findMaxConsecutiveOnes(self, nums):
    s=0
    max1=0
    for i in range(len(nums)):
        if nums[i]==1:
            s+=1
            max1=max(s,max1)
        else:
            s=0
    return max1