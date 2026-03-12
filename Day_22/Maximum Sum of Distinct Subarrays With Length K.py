class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        curr_sum = 0
        freq = {}
        max_sum = 0

        for right in range(len(nums)):

            curr_sum += nums[right]

            if nums[right] in freq:
                freq[nums[right]] += 1
            else:
                freq[nums[right]] = 1

            if right - left + 1 > k:
                freq[nums[left]] -= 1
                curr_sum -= nums[left]

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

            if right - left + 1 == k and len(freq) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum