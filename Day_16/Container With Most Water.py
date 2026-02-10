class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        maxarea=0
        r=len(height)-1
        while l<=r:
            w=r-l
            minhe=min(height[l],height[r])
            area=minhe*w
            maxarea=max(area,maxarea)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxarea
                        