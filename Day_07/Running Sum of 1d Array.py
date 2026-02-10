class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l1=[]
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            l1.append(sum)
        return l1