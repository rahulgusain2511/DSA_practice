def leaders(a, N):
         
        #optimal
        N=len(a)
        ans=[]
        maxi=a[N-1]
        ans.append(a[N-1])
        for i in range(N-2,-1,-1):
            if a[i]>maxi:
                ans.append(a[i])
            maxi=max(maxi,a[i])
        ans.sort()
        return ans


        # brute force
        ans=[]
        
        for i in range(N):
            leader=True
            for j in range (i+1,N):
                if A[i]<A[j]:
                    leader=False
                    break
            if leader==True:
                ans.append(A[i])
        return ans