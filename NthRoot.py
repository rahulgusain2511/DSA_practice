class Solution:
	def NthRoot(self, n, m):
		# Code here
		low,high=1,m
		while low<=high:
		    mid = (low+high)//2
		    if(pow(mid,n)==m):
		        return mid
		    if pow(mid,n)<m:
		        low=mid+1
		    else:
		        high=mid-1
        return -1