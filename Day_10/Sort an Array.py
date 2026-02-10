class Solution:
    def mergesortmerging(self,nums,l,mid,r):
        i=l
        j=mid+1
        res=[]
        while i<=mid and j<=r:
            if nums[i]<nums[j]:
                res.append(nums[i])
                i+=1
            else:
                res.append(nums[j])
                j+=1
        while i<=mid:
            res.append(nums[i])
            i+=1
        while j<=r:
            res.append(nums[j])
            j+=1
        dups=l
        for k in range(len(res)):
            nums[dups]=res[k]
            dups+=1
    def mergesortdiv(self,nums,l,r):
        if l>=r:
            return
        mid=(l+r)//2
        self.mergesortdiv(nums,l,mid)
        self.mergesortdiv(nums,mid+1,r)
        self.mergesortmerging(nums,l,mid,r)

    def sortArray(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        self.mergesortdiv(nums,l,r)
        return nums