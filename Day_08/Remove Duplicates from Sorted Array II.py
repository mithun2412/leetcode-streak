class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) <= 2:
            return len(nums)

        k = 1

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 1]:
                k += 1
                nums[k] = nums[i]

        return k + 1
