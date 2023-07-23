def findPages(arr,n,m):
    if m>len(arr):
        return -1
    
    low=0
    high=sum(arr)
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if isPossible(arr,n,m,mid):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans


def isPossible(arr,n,m,mid):
    student_cnt=1
    page_sum=0

    for i in range(n):
        if page_sum+arr[i]<=mid:
            page_sum+=arr[i]
        else:
            student_cnt+=1
            if student_cnt>m or arr[i]>mid:
                return False
            
            page_sum=0
            
            page_sum+=arr[i]
    return True
