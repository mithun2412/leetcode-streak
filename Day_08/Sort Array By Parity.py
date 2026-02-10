class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # l1=[]
        # for i in range(len(nums)):
        #     if nums[i]%2==0:
        #         l1.append(nums[i])
        # for i in range(len(nums)):
        #     if nums[i]% 2 !=0:
        #         l1.append(nums[i])
        # return l1
        start =0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[start],nums[i]=nums[i],nums[start]
                start+=1
        return nums