import math
def smallestDivisor(self, arr, limit):
        if len(arr)>limit:
            return -1
        ans=-1
        low=1
        high=max(arr)
        while low<=high:
            mid=(low+high)//2
            Sum=0

            for i in arr:
                Sum+=math.ceil(float(i)/float(mid))
            if Sum<=limit:
                ans=mid
                high=mid-1
                
                
                
                
            else:
                low=mid+1
                
                
               
                
        return ans
        

        
        '''

        brute force

        for div in range(1,max(arr)+1):
            sum=0
            for i in range(len(arr)):
                sum+=math.ceil(float(arr[i])/(div))
            if sum<=limit:
                return div
        return -1
        '''