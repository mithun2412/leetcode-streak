class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
        # max_sum = current_sum = nums[0]
        # for i in range(1, len(nums)):
        #     current_sum = max(nums[i], current_sum + nums[i])
        #     max_sum = max(max_sum, current_sum)
        # return max_sum
        currsum=0
        maxsum=nums[0]
        for i in range(len(nums)):
            currsum+=nums[i]
            if currsum>maxsum:
                maxsum=currsum
            if currsum<0:
                currsum=0
        return maxsum