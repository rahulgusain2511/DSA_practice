def majorityElement(nums):
    mpp={}
    for i in range(len(nums)):
        if nums[i] in mpp:
            mpp[nums[i]] += 1
        else:
            mpp[nums[i]] = 1

    for i in mpp.keys():
        if (mpp.get(i)>(len(nums))//2):
            return i

nums=[2,2,2,2,2,2,2,3,3,4,5,1]
print(majorityElement(nums))