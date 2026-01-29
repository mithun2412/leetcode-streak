class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nge = {}   # stores next greater for nums2 elements

        for num in nums2:
            while stack and stack[-1] < num:
                nge[stack.pop()] = num
            stack.append(num)

        # remaining elements have no next greater
        while stack:
            nge[stack.pop()] = -1

        return [nge[num] for num in nums1]
