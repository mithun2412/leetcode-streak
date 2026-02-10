import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        h=[]
        for x in range(len(nums)):
            heapq.heappush(h,nums[x])
            if len(h)>k:
                heapq.heappop(h)
        return h[0]
            
