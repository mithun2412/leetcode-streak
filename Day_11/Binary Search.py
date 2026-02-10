class Solution:
    def bs(self, nums, l, r, t):
        if l > r:
            return -1

        mid = (l + r) // 2

        if nums[mid] == t:
            return mid
        elif nums[mid] > t:
            return self.bs(nums, l, mid - 1, t)
        else:
            return self.bs(nums, mid + 1, r, t)

    def search(self, nums: List[int], target: int) -> int:
        return self.bs(nums, 0, len(nums) - 1, target)
