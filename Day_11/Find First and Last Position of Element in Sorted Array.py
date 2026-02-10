class Solution:
    def findLeft(self, nums, target):
        l, r = 0, len(nums) - 1
        ans = -1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                ans = m
                r = m - 1   # move left
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return ans

    def findRight(self, nums, target):
        l, r = 0, len(nums) - 1
        ans = -1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                ans = m
                l = m + 1   # move right
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.findLeft(nums, target), self.findRight(nums, target)]
