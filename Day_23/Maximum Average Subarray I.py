class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0
        
        # first window
        for i in range(k):
            window_sum += nums[i]
        
        max_sum = window_sum

        # sliding window
        for r in range(k, len(nums)):
            window_sum += nums[r]      # add new element
            window_sum -= nums[r-k]    # remove old element
            
            max_sum = max(max_sum, window_sum)

        return max_sum / k