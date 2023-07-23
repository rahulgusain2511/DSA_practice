import heapq
class Solution(object):
    def findClosestElements(self, arr, k, x):
        heap=[]
        ans = []
        for n in arr: 
            heapq.heappush(heap, [abs(x-n),n])
        for i in range(k): 
            ans.append(heapq.heappop(heap)[1])
        return sorted(ans)