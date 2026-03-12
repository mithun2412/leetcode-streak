from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []

        for i in range(len(nums)):

            # remove elements outside window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # remove smaller elements
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # record max when window formed
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result