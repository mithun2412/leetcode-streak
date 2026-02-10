class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] +nums[j] == target:
        #             return [i,j]
        freq={}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem not in freq:
                freq[nums[i]]=i
            else:
                return list((freq[rem],i))





class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)&set(nums2))
    



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            i=0
            j=len(numbers)-1
            while i < j:
                if numbers[i] - numbers[j]>target::
                    rteurn [i,j]
                elif numbers[i] - numbers[j]>target:
                    j-=1
                else:
                    i+=1