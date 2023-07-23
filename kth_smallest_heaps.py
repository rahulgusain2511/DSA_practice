import heapq
class Solution:
    def kthSmallest(self,arr, l, r, k):
        heaps=[]
        for i in arr:
            heapq.heappush(heaps,-i)
            if len(heaps) > k:
                heapq.heappop(heaps)
        return -heaps[0]
